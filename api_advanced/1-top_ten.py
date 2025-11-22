#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts.
    If not a valid subreddit, prints None.
    """
    # Reddit API endpoint
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    
    # Custom User-Agent is required to avoid "Too Many Requests" (429) errors
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/custom_user)"}
    
    # Parameters for the API request
    params = {"limit": 10}

    try:
        # allow_redirects=False is crucial.
        # Invalid subreddits redirect to a search page (status 302),
        # which we must treat as an invalid subreddit.
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        # Check for success. If status is 404 or 302 (redirect), it's invalid.
        if response.status_code != 200:
            print(None)
            return

        # Parse JSON
        results = response.json().get("data")
        
        # Double check that 'children' exists in the data
        if not results or "children" not in results:
            print(None)
            return

        children = results.get("children")
        
        # Loop through and print titles
        for post in children:
            print(post.get("data").get("title"))

    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten("python")
