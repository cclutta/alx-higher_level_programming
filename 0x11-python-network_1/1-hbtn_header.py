#!/usr/bin/python3
""" That fetches from URL
    Args:
        url: the url to fetch
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as res:
        print(res.getheader('X-Request-Id'))
