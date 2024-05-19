#!/usr/bin/env python3
# vim:sw=4:ts=4:et:

"""
Example of creating a board, placing some words, and searching for those.
"""

import sys
from wordsearch import WordsearchBoard

__author__ = "Andrei Belov"
__license__ = "MIT"
__copyright__ = f"Copyright (c) {__author__}"


def main():
    """
    Entry point
    """
    words = ["BEAR", "HAMSTER", "GOOSE", "MONKEY", "FOX"]

    ws = WordsearchBoard()

    for word in words:
        if ws.place_word(word):
            print(f":) word {word} placed on board")
        else:
            print(f":( word {word} could not be placed on board")

    print("\nBoard:")
    ws.print_board()

    for word in words:
        empty_grid = ws.empty_grid()
        word_found = ws.exists(word, res_board=empty_grid)

        print(f"\nSearching for {word}: {word_found}")
        if word_found:
            ws.print_board(grid=empty_grid)


if __name__ == "__main__":
    sys.exit(main())
