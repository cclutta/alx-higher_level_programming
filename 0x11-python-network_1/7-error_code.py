#!/usr/bin/python3
""" that takes in a URL, sends a request to the URL and displays response
    Args:
        url: the url to fetch
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
