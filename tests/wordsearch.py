"""
Tests for WordSearch
"""

import pytest
from wordsearch import WordsearchBoard
from wordsearch import EMPTY_CHAR as _ec


__author__ = "Andrei Belov"
__license__ = "MIT"
__copyright__ = f"Copyright (c) {__author__}"


TEST_BOARD1 = [
    ["X", "X", "X"],
    ["C", "A", "T"],
    ["X", "X", "X"],
]

TEST_BOARD2 = [
    ["X", "C", "X"],
    ["X", "A", "X"],
    ["X", "T", "X"],
]

TEST_BOARD3 = [
    ["C", "X", "X"],
    ["X", "A", "X"],
    ["X", "X", "T"],
]

TEST_BOARD4 = [
    ["X", "X", "C"],
    ["X", "A", "X"],
    ["T", "X", "X"],
]

TEST_BOARD5 = [
    ["X", "C", "X"],
    ["F", "A", "T"],
    ["X", "R", "X"],
]

TEST_BOARD6 = [
    ["C", _ec, _ec],
    [_ec, "A", _ec],
    [_ec, _ec, "T"],
]


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


def test_find_word_in_default_directions():
    """
    Find word in predefined board, default valid directions
    """
    for grid in [TEST_BOARD1, TEST_BOARD2, TEST_BOARD3, TEST_BOARD4]:
        wb = WordsearchBoard(width=3, height=3, grid=grid)
        empty_grid = wb.empty_grid()
        print("\n")
        assert wb.exists("CAT", res_board=empty_grid) is True
        wb.print_board(grid=empty_grid)
        assert wb.exists("DOG") is False


def test_find_word_in_unexpected_directions():
    """
    Find word in predefined board, unexpected directions
    """
    wb = WordsearchBoard(width=3, height=3, grid=TEST_BOARD5)

    for word in ["CAT", "FAR"]:
        assert wb.exists(word) is False

    for word in ["FAT", "CAR"]:
        assert wb.exists(word) is True


def test_find_word_in_all_directions():
    """
    Find word in predefined board, all possible directions (mixed)
    """
    wb = WordsearchBoard(width=3, height=3, grid=TEST_BOARD5)

    for word in ["CAT", "FAR", "XCATX", "XFATX", "XTAF", "TAFX"]:
        empty_grid = wb.empty_grid()
        assert wb.exists(word, res_board=empty_grid, direction="all") is True
        print(f"\n={word}=")
        wb.print_board(grid=empty_grid)


def test_place_and_find():
    """
    Place some words on a new board and try to find these
    """
    wb = WordsearchBoard(width=10, height=10)

    words = ["HAMSTER", "MONKEY", "GOOSE", "BEAR", "FOX"]

    for word in words:
        assert wb.place_word(word) is True

    print("Source board:")
    wb.print_board()

    for word in words:
        empty_grid = wb.empty_grid()
        assert wb.exists(word, res_board=empty_grid) is True
        print(f"\n={word}=")
        wb.print_board(grid=empty_grid)


def test_place_too_long_word():
    """
    Try to place a word with length exceeding board's dimensions
    """
    wb = WordsearchBoard(width=3, height=3)
    assert wb.place_word("CATFISH") is False


def test_place_and_find_limited_directions():
    """
    Place a word which could fit only in limited directions
    """
    for dimensions in [(10, 3), (3, 10)]:
        wb = WordsearchBoard(width=dimensions[0], height=dimensions[1])
        empty_grid = wb.empty_grid()
        assert wb.place_word("CATFISH") is True
        assert wb.exists("CATFISH", res_board=empty_grid) is True
        print(f"\n={dimensions}=")
        wb.print_board(grid=empty_grid)


def test_place_no_chance():
    """
    Try to place a word on a board without chance to success
    """
    wb = WordsearchBoard(width=3, height=3, grid=TEST_BOARD6)
    assert wb.place_word("FOG") is False
