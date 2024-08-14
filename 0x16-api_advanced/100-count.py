#!/usr/bin/python3
"""
recursive function that queries the Reddit API, parses the title
of all hot articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces)
"""


from collections import Counter
import json
import requests
import re


def count_words(subreddit, word_list, after=None, word_count=None):
    """This function counts the words of a
    given subreddit.
    """
    if word_count is None:
        word_count = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    if after:
        url += f"?after={after}"

    custom_user_agent = 'Gabriel/1.0 (by /u/Sea-Meet-212)'
    headers = {'User-Agent': custom_user_agent}
    response = requests.get(url, headers=headers, allow_redirects=False)
    # Checking for invalid subreddit
    if response.status_code == 302:
        return
    if response.status_code != 200:
        return

    data = response.json()
    posts = data['data']['children']
    for post in posts:
        title = post['data']['title']
        words = re.findall(r'\b\w+\b', title.lower())
        word_count.update({word: words.count(word)
                          for word in word_list if word in words})

    if 'after' in data['data'] and data['data']['after']:
        count_words(subreddit, word_list, data['data']['after'], word_count)
    else:
        sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print(f"{word}: {count}")
