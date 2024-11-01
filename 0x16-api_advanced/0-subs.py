#!/usr/bin/python3
"""
A module containing functions for working with the Reddit API.
"""


import requests


def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for a given subreddit.
    """
    response = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        allow_redirects=False,
        headers={"user-agent": "ubuntu_bot"},
        timeout=60,
    )

    return (
        response.json()["data"]["subscribers"]
        if response.status_code == 200
        else 0
    )
