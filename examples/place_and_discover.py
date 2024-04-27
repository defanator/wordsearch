#!/usr/bin/env python3
# vim:sw=4:ts=4:et:

"""
Example of creating a board, placing some words, and searching for those
"""

from wordsearch import WordsearchBoard

ws = WordsearchBoard()

words = ["BEAR", "HAMSTER", "GOOSE", "MONKEY", "FOX"]

for word in words:
    ws.place_word(word)

print("Board:")
ws.print_board()

for word in words:
    empty_grid = ws.empty_grid()
    word_found = ws.exists(word, res_board=empty_grid)

    print(f"Searching for {word}: {word_found}")
    if word_found:
        ws.print_board(grid=empty_grid)
