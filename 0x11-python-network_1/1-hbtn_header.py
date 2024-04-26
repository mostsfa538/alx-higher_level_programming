#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and displays
    the value of the X-Request-Id variable found in the header of the response
"""
import sys
import urllib.request

request = urllib.request.Request(sys.aargv[1])
with urllib.request.urlopen(request) as response:
    print(dict(response.headers).get('X-Request-Id'))
