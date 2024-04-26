#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL,
and displays the body of the response (decoded in utf-8)
"""
from sys import argv
import requests


if __name__ == '__main__':
    with requests.get(argv[1]) as response:
        print(
            response.text if response.ok
            else f'Error code: {response.status_code}'
        )
