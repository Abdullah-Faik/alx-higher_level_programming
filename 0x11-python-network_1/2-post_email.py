#!/usr/bin/python3
"""print type response """

from urllib import request, parse
from sys import argv


def main():
    """print request"""
    url = argv[1]
    email = argv[2]
    data = parse.urlencode({'email': email}).encode('ascii')
    with request.urlopen(str(url), data) as res:
        print(res.read().decode('utf-8'))


if __name__ == "__main__":
    main()
