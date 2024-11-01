#!/usr/bin/python3

"""
This script uses a recursive function to query the Reddit API and return a
list containing the titles of all hot articles for a given subreddit. It
prints a sorted count of the number of times each word appears in the titles
"""
import requests


def count_words(subreddit, word_list, found_list=[], next_page=None):
    """
    Prints counts of given words found in hot posts of a given subreddit.
    """
    try:
        response = requests.get(
            f"http://www.reddit.com/r/{subreddit}/hot.json?after={next_page}",
            headers={"user-agent": "nabuntu_bot-01"},
            timeout=60,
        )
    except requests.ConnectionError:
        print("Encountered a connection error. Please try again later.")
        return

    if next_page is None:
        word_list = [word.lower() for word in word_list]

    if response.status_code != 200:
        return

    data = response.json()["data"]
    next_page = data["after"]
    posts = data["children"]

    find_matching_words(word_list, found_list, posts)

    if next_page is not None:
        count_words(subreddit, word_list, found_list, next_page)
    else:
        word_count = count_word_occurrences(found_list)

        print_keywords_count(word_count)


def print_keywords_count(word_count):
    """
    Prints the keywords and their corresponding word counts in descending
    order.
    """
    sorted_word_count = sorted(
        word_count.items(), key=lambda item: item[1], reverse=True
    )

    for keyword, count in sorted_word_count:
        print("{}: {}".format(keyword, count))


def count_word_occurrences(found_list):
    """
    Counts the occurrences of each word in a given list.
    """
    word_count = {}
    for word in found_list:
        if word.lower() in word_count:
            word_count[word.lower()] += 1
        else:
            word_count[word.lower()] = 1
    return word_count


def find_matching_words(word_list, found_list, posts):
    """
    Finds and appends matching words from post titles to the found_list.
    """
    for post in posts:
        title = post["data"]["title"].lower()
        for word in title.split():
            if word in word_list:
                found_list.append(word)
