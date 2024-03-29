#!/usr/bin/python3
""" that takes in a URL and an email, sends a POST request to the passed URL
    Args:
        url: the url to fetch
        email: email to be passed
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    values = {"email": email}
    res = requests.post(url, data=values)
    print(res.text)
