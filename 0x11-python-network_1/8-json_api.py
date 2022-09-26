#!/usr/bin/python3
""" that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user
    Args:
        url: the url to fetch
        q: search term
"""

import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    values = {"q": q}
    res = requests.post(url, data=values)
    try:
        json = res.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
