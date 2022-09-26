#!/usr/bin/python3
""" script that takes GitHub Username and password and uses the
    GitHub API to display id
"""

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    
    auth = (username, password)

    url = "https://api.github.com/user"

    res = requests.get(url, auth=auth)
    json = res.json()

    print(json.get("id"))
