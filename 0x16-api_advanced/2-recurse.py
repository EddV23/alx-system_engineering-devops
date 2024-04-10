#!/usr/bin/python3
"""queries Reddit & returns list of titles of all hot articles for subreddit"""
import requests


def recurse(subreddit, hot_list=[], next="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "next": next,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    next = results.get("next")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if next is not None:
        return recurse(subreddit, hot_list, next, count)
    return hot_list