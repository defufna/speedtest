# Speedtest!

![Screenshot](/screenshot.png?raw=true)

## About

Simple speed test similar to various online tests, the benefit of this test is that it can be run locally. 

## Requirements

Python 3.4 (it might work on older Python3)

## Usage

Extract all files, navigate to folder and execute:

`python3 ./speedtest.py`

Open http://localhost:8000 in browser.
Click start to test download speed between your browser and the server. The server sends 64mb of data in 8 chunks, this can be changed by editing constants in speedtest.py.

If you want different port then 8000, pass it as an argument to speedtest.py.

`python3 ./speedtest.py 80`
