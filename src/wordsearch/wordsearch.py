#!/usr/bin/env python3
# vim:sw=4:ts=4:et:

"""
Wordsearch implementation
"""

import random
import string

EMPTY_CHAR = "-"


class WordsearchBoard:
    """
    Class representing a grid for word search board
    """

    def __init__(self, width=20, height=20, grid=None):
        if width < 1:
            raise ValueError("width must be greater than 0")

        if height < 1:
            raise ValueError("height must be greater than 0")

        self.width = width
        self.height = height

        if grid is not None:
            self.grid = grid
            return

        self.grid = None
        self.reset_grid()

    def reset_grid(self):
        """
        Reset grid with default empty char
        """
        del self.grid
        self.grid = []
        for y in range(self.height):
            self.grid.append([])
            for _ in range(self.width):
                self.grid[y].append(EMPTY_CHAR)

    def mask_grid(self):
        """
        Mask empty chars with random uppercase letters
        """
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == EMPTY_CHAR:
                    self.grid[y][x] = random.choice(string.ascii_uppercase)

    def occupied(self, y, x, radius=1):
        """
        Check if a given cell is already occupied with a letter

        :param y: int - row
        :param x: int - column
        :param radius: int - number of adjacent cells that must be empty as well
        :return: bool - true if occupied, false otherwise
        """
        if radius == 0:
            if self.grid[y][x] != EMPTY_CHAR:
                return True

            return False

        for yw in range(y - radius, y + radius + 1):
            for xw in range(x - radius, x + radius + 1):
                if yw < 0 or xw < 0:
                    continue
                if yw > self.height - 1 or xw > self.width - 1:
                    continue
                if self.grid[yw][xw] != EMPTY_CHAR:
                    return True

        return False

    def find_xy(self, wlen, max_attempts=1000):
        # pylint: disable=R0912
        """
        Find coordinates and direction for a word with a given length

        :param wlen: int - length of a word
        :param max_attempts: int - max number of attempts to find a place
        :return: int x, int y, tuple direction - coordinates and direction for a word
        :return: None if free cell was not found
        """
        if self.width < wlen and self.height < wlen:
            return False

        if wlen <= self.height and wlen <= self.width:
            direction_choices = [[1, 0], [1, 1], [0, 1], [1, -1]]

        elif self.width < wlen <= self.height:
            direction_choices = [[1, 0]]

        elif self.height < wlen <= self.width:
            direction_choices = [[0, 1]]

        y_spacing = self.height - wlen + 1
        x_spacing = self.width - wlen + 1

        i = 0
        while True:
            i += 1
            direction = random.choice(direction_choices)

            if direction[0] == 1:
                y = random.randrange(0, y_spacing) if y_spacing > 0 else 0

            elif direction[0] == 0:
                y = random.randrange(0, self.height)

            if direction[1] == -1:
                x = random.randrange(wlen - 1, self.width)

            elif direction[1] == 1:
                x = random.randrange(0, x_spacing) if x_spacing > 0 else 0

            else:  # direction[1] == 0
                x = random.randrange(0, self.width)

            fits = True
            for c in range(wlen):
                if self.occupied(y + direction[0] * c, x + direction[1] * c):
                    fits = False
                    break

            if fits:
                return x, y, direction

            if i > max_attempts:
                break

        return None

    def place_word(self, word):
        """
        Place a word to grid

        :param word: str - word to place
        :return: bool - true if word was placed, false otherwise
        """
        wlen = len(word)

        x, y, direction = self.find_xy(wlen)

        if x is None:
            return False

        for c in range(wlen):
            self.grid[y + direction[0] * c][x + direction[1] * c] = word[c]

        return True

    def exists(self, word, res_board=None, direction="default"):
        """
        Check whether a given word present on a board

        :param word: str - word to search
        :param res_board: WordsearchBoard.grid - grid with a given word if it was found
        :param direction: str - which directions to look for
        :return: bool - true if a word was found, false otherwise
        """
        for y in range(self.height):
            for x in range(self.width):
                if word[0] == self.grid[y][x]:
                    if self.find(word, y, x, res_board=res_board, direction=direction):
                        return True

        return False

    def find(self, word, row, col, i=0, direction="default", res_board=None):
        # pylint: disable=R0913
        """
        Recursive function for locating a word

        :param word: str - word to search
        :param row: row in a grid (y axis)
        :param col: column in a grid (x axis)
        :param i: int - current position in a word
        :param direciton: str - searching direction
        :param res_board: WordsearchBoard.grid - grid for storing results
        :return: bool - true if word was found, false otherwise
        """
        # print(f'find called: word={word} row={row} col={col} i={i}')
        if i == len(word):
            return True

        if row < 0 or row >= self.height:
            return False

        if col < 0 or col >= self.width:
            return False

        if word[i] != self.grid[row][col]:
            return False

        self.grid[row][col] = "*"

        if direction == "default":
            res = (
                self.find(word, row + 1, col, i + 1, res_board=res_board)
                or self.find(word, row - 1, col, i + 1, res_board=res_board)
                or self.find(word, row, col + 1, i + 1, res_board=res_board)
                or self.find(word, row, col - 1, i + 1, res_board=res_board)
                or self.find(
                    word,
                    row + 1,
                    col + 1,
                    i + 1,
                    res_board=res_board,
                    direction=direction,
                )
                or self.find(
                    word,
                    row - 1,
                    col - 1,
                    i + 1,
                    res_board=res_board,
                    direction=direction,
                )
                or self.find(
                    word,
                    row + 1,
                    col - 1,
                    i + 1,
                    res_board=res_board,
                    direction=direction,
                )
                or self.find(
                    word,
                    row - 1,
                    col + 1,
                    i + 1,
                    res_board=res_board,
                    direction=direction,
                )
            )

        elif direction == "horizontal":
            res = self.find(
                word, row, col + 1, i + 1, res_board=res_board, direction=direction
            ) or self.find(
                word, row, col - 1, i + 1, res_board=res_board, direction=direction
            )

        elif direction == "vertical":
            res = self.find(
                word, row + 1, col, i + 1, res_board=res_board, direction=direction
            ) or self.find(
                word, row - 1, col, i + 1, res_board=res_board, direction=direction
            )

        elif direction == "diagonal_cross1":
            res = self.find(
                word, row + 1, col + 1, i + 1, res_board=res_board, direction=direction
            ) or self.find(
                word, row - 1, col - 1, i + 1, res_board=res_board, direction=direction
            )

        elif direction == "diagonal_cross2":
            res = self.find(
                word, row + 1, col - 1, i + 1, res_board=res_board, direction=direction
            ) or self.find(
                word, row - 1, col + 1, i + 1, res_board=res_board, direction=direction
            )

        self.grid[row][col] = word[i]

        if res and res_board:
            res_board[row][col] = word[i]

        return res

    def print_board(self, grid=None):
        """
        Print board

        :param grid: WordsearchBoard.grid - grid to print
        """
        if not grid:
            grid = self.grid

        for row in grid:
            print(" ".join(row))

    def empty_grid(self):
        """
        Create empty grid object (2D-array) and return it

        :return: WordsearchBoard.grid - empty grid with a size of original board
        """
        grid = []
        for y in range(self.height):
            grid.append([])
            for _ in range(self.width):
                grid[y].append(EMPTY_CHAR)

        return grid
