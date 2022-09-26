#!/usr/bin/python3
""" script that takes GitHub Username and password and uses the
    GitHub API to display id
"""

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/" + username
    headers = {'Authorization': 'Bearer ' + password}

    res = requests.get(url, headers=headers)
    res = res.json()

    print(res.get("id"))
