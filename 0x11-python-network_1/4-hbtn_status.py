#!/usr/bin/python3
"""print type response """

import requests


def main():
    """print request"""
    url = 'https://alx-intranet.hbtn.io/status'
    with requests.get(url) as r:
        print(
            'Body response:\n'
            f'\t- type: {type(r.text)}\n'
            f'\t- content: {r.text}'
        )


if __name__ == "__main__":
    main()
