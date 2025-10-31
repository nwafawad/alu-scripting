#!/usr/bin/python3
"""
0-subs.py

This module provides a function to query the Reddit API and return the
number of subscribers for a given subreddit.

Functions:
    number_of_subscribers(subreddit): Returns the subscriber count for
    the specified subreddit, or 0 if the subreddit is invalid or
    inaccessible.

Usage (as import):
    >>> from subs import number_of_subscribers
    >>> print(number_of_subscribers("python"))
    1234567

Usage (as script):
    $ python3 0-subs.py python
    1234567
"""

import requests
import sys


def number_of_subscribers(subreddit):
    """
    Query the Reddit API to get the number of subscribers for a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers if the subreddit exists,
             otherwise 0.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "alu-scripting:sub_count:v1.0 (by /u/yourusername)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data", {})
            return data.get("subscribers", 0)
        return 0
    except Exception:
        return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <subreddit>".format(sys.argv[0]))
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
