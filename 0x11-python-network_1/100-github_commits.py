#!/usr/bin/python3
""" script that lists last ten commits of a repo of a user
"""

import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos/"+owner+"/"+repo+"/commits?per_page=10"
    
    res = requests.get(url)
    commits = res.json()
    
    for commit in commits:
        print("{}: {}".format(commit.get("sha"),
                              commit.get("commit").get("author").get("name")))
