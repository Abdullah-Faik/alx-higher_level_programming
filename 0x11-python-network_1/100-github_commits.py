#!/usr/bin/python3
"""
Lists 10 commits (from the most recent to oldest)
"""
from sys import argv
import requests


if __name__ == '__main__':
    url = f'https://api.github.com/repos/{argv[2]}/{argv[1]}/commits'
    params = {
        'per_page': 10
    }
    with requests.get(url, params=params) as response:
        if response.ok:
            commits = response.json()
            for commit in commits:
                print(
                    f'{commit["sha"]}: '
                    f'{commit["commit"]["author"]["name"]}'
                )
        else:
            print(response.status_code)
