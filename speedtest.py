#!/usr/bin/env python3

# This file is part of Speedtest.
#
# Speedtest is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Speedtest is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Speedtest.  If not, see <http://www.gnu.org/licenses/>.


from http.server import HTTPServer, SimpleHTTPRequestHandler
import sys
import random

CHUNK_SIZE = 1024*1024*8
CHUNK_COUNT = 8

CHUNK = bytes(random.getrandbits(8) for _ in range(CHUNK_SIZE))

class SpeedTest(SimpleHTTPRequestHandler):
	def __init__(self, *args):
		SimpleHTTPRequestHandler.__init__(self, *args)

	def do_GET(self):
		if self.path == "/speedtest":
			self.speedtest()
			return
		elif self.path in ["/", "/index.html"]:			
			SimpleHTTPRequestHandler.do_GET(self)
		else:			
			SimpleHTTPRequestHandler.send_error(self, 404, "Page not found")

	def speedtest(self):
		self.protocol_version='HTTP/1.1'
		self.send_response(200, 'OK')
		self.send_header('Content-type', 'application/octet-stream	')
		self.send_header('Content-Length', CHUNK_SIZE*CHUNK_COUNT)
		self.end_headers()
		
		for i in range(CHUNK_COUNT):
			self.wfile.write(CHUNK)

def main():
	port = 8000 if len(sys.argv) == 1 else int(sys.argv[1])    
	print("Serving on {0}".format(port))
	server = HTTPServer(('', port), SpeedTest)
	server.serve_forever()


if __name__ == "__main__":
	main()