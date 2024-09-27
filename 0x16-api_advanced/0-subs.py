#!/usr/bin/python3
"""
Module 0-subs
This module contains a function that queries the Reddit API to get the number of subscribers of a subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'my-app/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    print(f"Status Code: {response.status_code}")  
    if response.status_code == 200:
        data = response.json()
        print(data)  
        return data.get('data', {}).get('subscribers', 0)
    else:
        return 0  
