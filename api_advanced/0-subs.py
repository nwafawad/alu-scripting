#!/usr/bin/python3
"""
Reddit API: number_of_subscribers

This module defines a function that queries the Reddit API and returns
the total number of subscribers for a given subreddit.
"""

import requests
import sys

def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers for a subreddit, or 0 if invalid.
    """
    if not isinstance(subreddit, str) or not subreddit:
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "alu-scripting-task0:nawaf/1.0 (contact: example@example.com)"
    }

    try:
        # Do not follow redirects to avoid search-result fallbacks
        resp = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
    except requests.RequestException:
        return 0

    if resp.status_code != 200:
        return 0

    try:
        data = resp.json()
    except ValueError:
        return 0

    return int(data.get("data", {}).get("subscribers", 0))


if __name__ == "__main__":
    """
    Entry point for command-line execution.
    """
    if len(sys.argv) < 2:
        print("Usage: ./0-subs.py <subreddit>")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
