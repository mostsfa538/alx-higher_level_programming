#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays
   the body of the response (decoded in utf-8)
   using requests package
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code == 2:
        print(r.text)
    else:
        print(f"Error code: {r.status_code}")
