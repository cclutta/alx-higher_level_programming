#!/usr/bin/python3
""" that takes in a URL, sends a request to the URL and displays response
    Args:
        url: the url to fetch
"""

import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
