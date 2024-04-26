#!/usr/bin/python3
"""script that takes 2 arguments to list 10 commits
   (from the most recent to oldest)
"""
import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    r = requests.get(url)
    data = r.json()

    i = 0

    try:
        for item in list(data):
            if i == 10:
                break
            print(f"{item.get('sha')}:",
                  item.get('commit').get('author').get('name'))
            i += 1
    except IndexError:
        pass
