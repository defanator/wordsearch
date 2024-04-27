"""
Tests for WordSearch
"""

import pytest
from wordsearch import WordsearchBoard


__author__ = "Andrei Belov"
__license__ = "MIT"
__copyright__ = f"Copyright (c) {__author__}"


def test_create_default_board():
    """
    Create default board
    """
    wb = WordsearchBoard()
    assert isinstance(wb, WordsearchBoard)
    assert wb.width == 20
    assert wb.height == 20
    assert len(wb.grid) == wb.height
    assert len(wb.grid[0]) == wb.width


def test_create_custom_board():
    """
    Create custom board
    """
    wb = WordsearchBoard(width=3, height=3)
    assert isinstance(wb, WordsearchBoard)
    assert wb.width == 3
    assert wb.height == 3
    assert len(wb.grid) == wb.height
    assert len(wb.grid[0]) == wb.width


def test_create_board_with_invalid_input():
    """
    Create custom board with invalid input values
    """
    with pytest.raises(ValueError, match=r"width must be greater than 0"):
        _ = WordsearchBoard(width=-3, height=3)

    with pytest.raises(ValueError, match=r"height must be greater than 0"):
        _ = WordsearchBoard(width=3, height=-3)
