"""
Common functions for WordSearch tests
"""

from wordsearch import EMPTY_CHAR as _ec

__author__ = "Andrei Belov"
__license__ = "MIT"
__copyright__ = f"Copyright (c) {__author__}"


def grid_contains_empty_chars(wb):
    for y in range(wb.height):
        for x in range(wb.width):
            if wb.grid[y][x] == _ec:
                return True

    return False
