#!/usr/bin/python3
"""Write a function that queries
the Reddit API and returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    user_agent = {'User-agent': 'Mozilla/5.0'}
    try:
        req = requests.get('https://www.reddit.com/r/{}/about.json'
                           .format(subreddit), headers=user_agent)
        subscribers = req.json().get('data')
        return subscribers.get('subscribers')
    except Exception:
        return 0
