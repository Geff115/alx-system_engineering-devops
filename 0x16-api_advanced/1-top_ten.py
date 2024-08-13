#!/usr/bin/python3
"""
This function queries the Reddit API and
prints the titles of the first 10
hot posts listed for a given subreddit
"""


import requests


def top_ten(subreddit):
    """This function returns the first 10
    hot posts listed for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    custom_user_agent = 'Gabriel/1.0 (by /u/Sea-Meet-212)'
    headers = {'User-Agent': 'custom_user_agent'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            children_list = data['data']['children']
            titles = []
            for item in children_list:
                titles.append(item['data']['title'])
            for title in titles:
                print(title)
        else:
            print(None)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
