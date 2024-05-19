#!/usr/bin/env python3

"""
Example of creating a board and populating it with words from random Wikipedia article.
"""

import sys
import random
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from wordsearch import WordsearchBoard


__author__ = "Andrei Belov"
__license__ = "MIT"
__copyright__ = f"Copyright (c) {__author__}"


WIKI_RANDOM_ARTICLE_URL = "https://en.wikipedia.org/wiki/Special:Random"

GRID_SIZE = 25
NUM_WORDS = 15
WORD_MIN_LENGTH = 6


def get_nouns_from_random_wiki_article(word_min_length=WORD_MIN_LENGTH):
    """
    Get all nouns (in singular form) from a random Wikipedia article.
    """
    try:
        page = requests.get(WIKI_RANDOM_ARTICLE_URL, timeout=5)
    except requests.exceptions.RequestException as exc:
        print(exc)
        return None

    soup = BeautifulSoup(page.text, "html.parser")
    title = soup.find("title").get_text()

    text = ""
    for para in soup.find_all("p"):
        text = text + " " + para.get_text()

    tb = TextBlob(text)

    nouns = set()
    for t in tb.tags:
        if not t[0].isalpha():
            continue

        if t[1] in ("NN"):
            if len(t[0]) < word_min_length:
                continue

            nouns.add(t[0].upper())
            continue

        if t[1] in ("NNS"):
            singular = t[0].singularize()
            if len(singular) < word_min_length:
                continue

            nouns.add(singular.upper())
            continue

    return page.url, title, nouns


def hunt_for_words(num_words=NUM_WORDS, word_min_length=WORD_MIN_LENGTH):
    """
    Go through random Wikipedia articles and search for a required number
    of words with a given minimal length.
    """
    while True:
        try:
            url, title, nouns = get_nouns_from_random_wiki_article(
                word_min_length=word_min_length
            )
        except TypeError:
            return None

        if len(nouns) < num_words:
            continue

        break

    return url, title, random.sample(list(nouns), num_words)


def main():
    """
    Entrypoint.
    """
    try:
        url, title, nouns = hunt_for_words()
    except TypeError:
        return 1

    print(f"{title} ({url})\n")

    ws = WordsearchBoard(width=GRID_SIZE, height=GRID_SIZE)

    # chances are higher if we go from longest word down to shortest
    for w in sorted(nouns, key=len, reverse=True):
        if not ws.place_word(w):
            print(f"failed to place word: {w}")
            return 1

    for w in sorted(nouns):
        print(w)

    print()
    ws.mask_grid()
    ws.print_board()

    return 0


if __name__ == "__main__":
    sys.exit(main())
