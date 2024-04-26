#!/usr/bin/python3
""" script that takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""
import sys
import requests


if __name__ == "__main__":
    info = (sys.argv[1], sys.argv[2])
    pasword = url = 'https://api.github.com/user'

    r = requests.post(url, info)
    data = r.json()
    print("{}".format(data.get('id')))
