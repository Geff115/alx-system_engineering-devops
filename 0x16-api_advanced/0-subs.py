#!/usr/bin/python3
"""
This script queries a Reddit API and returns
the number of subscribers for a given subreddit
"""


import requests


def number_of_subscribers(subreddit):
    """This function queries the Reddit API and
    returns the number of subscribers.
    """
    if subreddit is None:
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    custom_user_agent = 'Gabriel/1.0 (by /u/Sea-Meet-212)'

    headers = {'User-Agent': 'custom_user_agent'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
