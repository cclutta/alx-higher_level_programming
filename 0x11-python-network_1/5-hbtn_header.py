#!/usr/bin/python3
""" That fetches and displays the value of the variable
    X-Request-Id in the response header
    Args:
        url: the url to fetch
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    content = requests.get(url)
    print(content.headers.get('X-Request-Id'))
