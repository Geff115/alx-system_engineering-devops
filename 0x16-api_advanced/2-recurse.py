#!/usr/bin/python3
"""
This script handle pagination by keeping track of
the after parameter provided by the Reddit API
"""


import requests
after = None


def recurse(subreddit, hot_list=[]):
    """This function queries the Reddit API and returns
    a list containing the titles of all hot articles
    for a given subreddit.
    """
    def fetch_hot_articles(after=None):
        """This function uses the after parameter in the URL
        for the recursive call to handle pagination.
        """
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        custom_user_agent = 'Gabriel/1.0 (by /u/Sea-Meet-212)'
        headers = {'User-Agent': custom_user_agent}

        params = {}
        if after:
            params['after'] = after

        try:
            response = requests.get(url, headers=headers, params=params,
                                    allow_redirects=False)
            if response.status_code != 200:
                return None, None

            data = response.json()
            children_list = data['data']['children']
            for item in children_list:
                hot_list.append(item['data']['title'])

            after = data['data']['after']
            return hot_list, after
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None, None

    hot_list, after = fetch_hot_articles()
    if hot_list is None:
        return None
    if after:
        hot_list, _ = fetch_hot_articles(after)

    return hot_list
