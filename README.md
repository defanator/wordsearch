# Word Search
#### Video Demo: https://youtu.be/cVwDebCU9CY
#### Description: WordSearch implementation in Python

[Word Search](https://en.wikipedia.org/wiki/Word_search) implementation in Python for [CS50x](https://cs50.harvard.edu/x/2024/) final project.

## Purpose

This project provides the `wordsearch` Python module exposing an interface to work with WordSearch boards (or grids). It can be used for both creating new boards from a list of given words and discovering given words on existing boards.

It also includes a couple of [examples](examples/README.md) to demonstrate the usage of a module.

## Module

The main module is [src/wordsearch/wordsearch.py](src/wordsearch/wordsearch.py). It provides the base `WordsearchBoard` class with the following methods:

 - `__init__` - class constructor
 - `reset_grid` - fills grid with default empty character
 - `mask_grid` - masks all non-empty characters in a grid with random uppercase letters
 - `occupied` - checks if a given position in a grid is occupied with non-empty character
 - `find_xy` - finds position and direction for a word of a given length in a grid (recursive function)
 - `place_word` - tries to place a word to a grid
 - `exists` - verifies if a given word present in a grid
 - `find` - searches for a given word in a given direction (recursive function)
 - `print_board` - prints a board
 - `empty_grid` - fills a grid with default empty character

## Design choices

### Default directions for words

While `WordsearchBoard.find()` recursive function can look for a word in all possible directions and even with mixed cases ("snaking puzzles"), it was clear that conventional directions in classic wordsearch puzzles basically include horizontal, vertical, and diagonal placing. Therefore, the `WordsearchBoard.exists()` method limits the default directions to conventional ones, and executes recursive `find()` function for every direction separately.

See `test_find_word_in_unexpected_directions()` and `test_find_word_in_all_directions()` tests for examples of how that could be rearranged (if required).

### Word spacing

The `WordsearchBoard.occupied()` function is using the `word_spacing` class attribute to decide how many adjacent cells of a given position in a grid must not be occupied when looking for a place for a new word. By default it is set to 1. For small boards it could be reduced to 0, for larger boards it may be increased to avoid possible word snuggling.

### Reversed words

Initial versions of the module included random reversing of a given word in `WordsearchBoard.place_word()`. That behavior was removed at a later stage to produce more conventional-looking puzzles.

## Tests

[Basic tests](tests/) are provided for checking module's functionality. Tests are written in Python and use [pytest](https://docs.pytest.org/) to operate. In the [original project](https://github.com/defanator/wordsearch) hosted on GitHub, these are running as a part of CI integration via GitHub actions (see e.g. [this run](https://github.com/defanator/wordsearch/actions/runs/9146900349) for details).

## Auxiliary files

Here is the list of other files in project's root and their meaning:

 - [Makefile](Makefile) - top-level Makefile for building the Python package, running tests/linters/formatters, creating virtualenvs, installing extra data for examples
 - [LICENSE](LICENSE) - project license
 - [pyproject.toml](pyproject.toml) - project configuration for Python package builders
 - [pytest.ini](pytest.ini) - default options for `pytest`
 - [tox.ini](tox.ini) - configuration for [tox](https://tox.wiki/), a tool used for running package builds, tests, linters, formatters, etc (if you're on CS50 codespace, make sure to install it with `pip install tox` before running corresponding make targets)

# Examples

See [examples documentation](examples/README.md) for details on how to run sample programs leveraging the `wordsearch` module.

In general, creating virtualenv with extra modules for Wikipedia example + fetching NLTK data are prerequisite steps:
```
project/ $ make venv venv-examples
[..]
Installing collected packages: urllib3, tqdm, soupsieve, regex, joblib, idna, click, charset-normalizer, certifi, requests, nltk, beautifulsoup4, textblob
Successfully installed beautifulsoup4-4.12.3 certifi-2024.6.2 charset-normalizer-3.3.2 click-8.1.7 idna-3.7 joblib-1.4.2 nltk-3.8.1 regex-2024.5.15 requests-2.32.3 soupsieve-2.5 textblob-0.18.0.post0 tqdm-4.66.4 urllib3-2.2.2

project/ $ make nltk_data
[..]
[nltk_data] Downloading package brown to
[nltk_data]     /workspaces/1309027/project/.venv/nltk_data...
[nltk_data]   Unzipping corpora/brown.zip.
[nltk_data] Downloading package punkt to
[nltk_data]     /workspaces/1309027/project/.venv/nltk_data...
[nltk_data]   Unzipping tokenizers/punkt.zip.
[nltk_data] Downloading package wordnet to
[nltk_data]     /workspaces/1309027/project/.venv/nltk_data...
[nltk_data] Downloading package averaged_perceptron_tagger to
[nltk_data]     /workspaces/1309027/project/.venv/nltk_data...
[nltk_data]   Unzipping taggers/averaged_perceptron_tagger.zip.
[nltk_data] Downloading package conll2000 to
[nltk_data]     /workspaces/1309027/project/.venv/nltk_data...
[nltk_data]   Unzipping corpora/conll2000.zip.
[nltk_data] Downloading package movie_reviews to
[nltk_data]     /workspaces/1309027/project/.venv/nltk_data...
[nltk_data]   Unzipping corpora/movie_reviews.zip.
Finished.
```

After the above steps, activate virtualenv:
```
project/ $ source ./.venv/bin/activate
(.venv) project/ $
```

Then run the examples:
```
(.venv) project/ $ ./examples/place_and_discover.py
:) word BEAR placed on board
:) word HAMSTER placed on board
:) word GOOSE placed on board
:) word MONKEY placed on board
:) word FOX placed on board

Board:
[..]

(.venv) project/ $ ./examples/create_board_from_wikipedia.py
Francesca Alexander - Wikipedia (https://en.wikipedia.org/wiki/Francesca_Alexander)

CHARITY
COLLECTION
COUSIN
CUSTOM
[..]
```

# Copyright

Copyright © 2024 Andrei Belov. Released under the [MIT License](LICENSE).
