#!/usr/bin/python3
"""print type response """

from urllib import request, parse
from urllib.error import HTTPError
from sys import argv


def main():
    """print request"""
    url = argv[1]
    try:
        with request.urlopen(str(url)) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as error:
        print(f'Error code: {error.code}')


if __name__ == "__main__":
    main()
