#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password),
and uses the GitHub API to display your id
"""
from sys import argv
import requests


if __name__ == '__main__':
    url = f'https://api.github.com/users/{argv[1]}'
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {argv[2]}',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    with requests.get(url, headers=headers) as response:
        if response.ok:
            try:
                result = response.json()
                if result == {}:
                    print('No result')
                else:
                    print(result.get("id"))
            except Exception:
                print('Not a valid JSON')
        else:
            print(None)
