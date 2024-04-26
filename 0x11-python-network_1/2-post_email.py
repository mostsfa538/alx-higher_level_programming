#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to the passed
   URL with the email as a parameter,
   and displays the body of the response (decoded in utf-8)"""
import sys
import urllib


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'enail': email})
    data = data.encode('utf-8')

    with urllib.request.urlopen(url, data=data) as response:
        print(response.read().decoded('utf-8'))
