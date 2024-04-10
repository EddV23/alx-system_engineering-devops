#!/usr/bin/python3
"""queries Reddit,parses title of hotarticles,sorts&prints count of keywords"""
import requests


def count_words(subreddit, word_list, instances={}, next="", count=0):
    """Prints sorted counts of keywords in hot articles of a given subreddit

    Args:
        subreddit (str): subreddit to be searched
        word_list (list): list of words to search for in articles' titles
        instances (obj): Key/value pairs of words/counts
        next (str): parameter of the next page of the API results
        count (int): parameter of results matched thus far
    """
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
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("next")
    count += results.get("dist")
    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if next is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, next, count)