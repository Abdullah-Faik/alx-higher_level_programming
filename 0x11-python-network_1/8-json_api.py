#!/usr/bin/python3
"""
takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
from sys import argv
import requests


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': argv[1] if len(argv) >= 2 else ""}
    with requests.post(url, data=data) as response:
        try:
            result = response.json()
            if result == {}:
                print('No result')
            else:
                print(f'[{result.get("id")}] {result.get("name")}')
        except Exception:
            print('Not a valid JSON')
