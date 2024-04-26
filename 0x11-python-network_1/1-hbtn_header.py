#!/usr/bin/python3
"""print type response """

from urllib import request
from sys import argv


def main():
    """print request"""
    url = argv[1]
    with request.urlopen(str(url)) as res:
        print(res.headers.get('X-Request-Id'))


if __name__ == "__main__":
    main()
