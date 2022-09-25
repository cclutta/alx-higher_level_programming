#!/usr/bin/python3
""" that takes in a URL and an email, sends a POST request to the passed URL
    Args:
        url: the url to fetch
        email: email to be passed
"""

import sys
from urllib import request, parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    values = {"email": email}
    data = parse.urlencode(values).encode('utf-8')
    with request.urlopen(url, data) as res:
        print(res.read().decode('utf-8'))
