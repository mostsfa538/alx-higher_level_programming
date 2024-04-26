#!/usr/bin/python3
"""script that takes in a letter and sends
   a POST request to http://0.0.0.0:5000/search_user
"""
import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
        data = r.json()

        if not data:
            print('No result')
        else:
            print("[{}] {}".format(data.get('id'), data.get('name')))
    except ValueError:
        print("Not a valid JSON")
