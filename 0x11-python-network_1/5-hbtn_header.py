#!/usr/bin/python3
"""
Sends a request to a given URL and displays the value of the variable
X-Request-Id in the response header

Usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
