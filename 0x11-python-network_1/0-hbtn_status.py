#!/usr/bin/python3
"""print type response """

from urllib import request


def main():
    """print request"""
    with request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        body = res.read()
        print(
            'Body response:\n'
            f'\t- type: {type(body)}\n'
            f'\t- content: {body}\n'
            f'\t- utf8 content: {body.decode("utf-8")}'
        )


if __name__ == "__main__":
    main()
