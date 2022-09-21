#!/usr/bin/python3
"""Write a function that queries
the Reddit API and returns the number of subscribers"""

import requests


def top_ten(subreddit):
    top_ten = []
    user_agent = {'User-agent': 'Mozilla/5.0'}
    try:
        req = requests.get('https://www.reddit.com/r/{}/hot.json'
                           .format(subreddit), headers=user_agent)
        top = req.json().get('data').get('children')
        for x in top:
            title = x.get('data').get('title')
            top_ten.append(title)
        for x in range(10):
            print(top_ten[x])
    except Exception:
        return 0
