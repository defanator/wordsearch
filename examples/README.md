# Examples

This directory contains a couple of example programs that demonstrate usage of the wordsearch module:

1. [place_and_discover.py](place_and_discover.py) - simple demo of placing a list of words to a board and running discovery against each word.
2. [create_board_from_wikipedia.py](create_board_from_wikipedia.py) - extended demo of creating a board from random Wikipedia article.

# Prerequisites

While 1st program is quite simple and does not require any extra dependencies, 2nd one is a bit more complicated.
It uses a few extra modules under the hood to do various things, in particular:

 - [requests](https://requests.readthedocs.io/en/latest/) to fetch resources from Wikipedia,
 - [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to parse HTML pages and extract text from paragraphs,
 - [NLTK](https://www.nltk.org/) and [TextBlob](https://textblob.readthedocs.io/en/dev/) to look for all common nouns in a given text and put every noun to singular form.

In order to create an isolated environment with all the modules available, please ensure you have Python and [virtualenv](https://virtualenv.pypa.io/en/latest/) installed first and run `make venv venv-examples nltk_data` from project's root directory:

```
[2024-05-19 08:49:49] defan@defmbp wordsearch % make venv venv-examples nltk_data
tox devenv --list-dependencies .venv
[..]
Installing collected packages: urllib3, tqdm, soupsieve, regex, joblib, idna, click, charset-normalizer, certifi, requests, nltk, beautifulsoup4, textblob
Successfully installed beautifulsoup4-4.12.3 certifi-2024.2.2 charset-normalizer-3.3.2 click-8.1.7 idna-3.7 joblib-1.4.2 nltk-3.8.1 regex-2024.5.15 requests-2.31.0 soupsieve-2.5 textblob-0.18.0.post0 tqdm-4.66.4 urllib3-2.2.1
[..]
mkdir -p /Users/defan/git/wordsearch/.venv/nltk_data
NLTK_DATA="/Users/defan/git/wordsearch/.venv/nltk_data" /Users/defan/git/wordsearch/.venv/bin/python3 -m textblob.download_corpora
[nltk_data] Downloading package brown to
[nltk_data]     /Users/defan/git/wordsearch/.venv/nltk_data...
[nltk_data]   Unzipping corpora/brown.zip.
[nltk_data] Downloading package punkt to
[nltk_data]     /Users/defan/git/wordsearch/.venv/nltk_data...
[nltk_data]   Unzipping tokenizers/punkt.zip.
[nltk_data] Downloading package wordnet to
[nltk_data]     /Users/defan/git/wordsearch/.venv/nltk_data...
[nltk_data] Downloading package averaged_perceptron_tagger to
[nltk_data]     /Users/defan/git/wordsearch/.venv/nltk_data...
[nltk_data]   Unzipping taggers/averaged_perceptron_tagger.zip.
[nltk_data] Downloading package conll2000 to
[nltk_data]     /Users/defan/git/wordsearch/.venv/nltk_data...
[nltk_data]   Unzipping corpora/conll2000.zip.
[nltk_data] Downloading package movie_reviews to
[nltk_data]     /Users/defan/git/wordsearch/.venv/nltk_data...
[nltk_data]   Unzipping corpora/movie_reviews.zip.
Finished.
```

This should create a [virtualenv](https://virtualenv.pypa.io/en/latest/) (in the `.venv` directory) with all the modules and NLTK data.

# Have some fun!

Once the environment is ready, you should activate it by running `source ./.venv/bin/activate` in your terminal and then run the 2nd example program (note that if you're using VSCode, it would automatically let you use Python interpreter from detected `.venv` virtualenv, so activating might not be explicitly required):

```
[2024-05-19 08:50:22] defan@defmbp wordsearch % source ./.venv/bin/activate

(.venv) [2024-05-19 09:21:31] defan@defmbp wordsearch % ./examples/create_board_from_wikipedia.py
Bachelor of Music - Wikipedia (https://en.wikipedia.org/wiki/Bachelor_of_Music)

BANKING
CAMPUSE
COMPLETION
CONSIST
DEGREE
FRONTRUNNER
HISTORY
MUSICOLOGY
PREPARATORY
PROGRAM
RECIPIENT
STANDARD
SUBJECT
THEORY
THERAPY

K F U W N C E N Y K M M U J V K E U Y U G N E P H
V A J R E C I P I E N T K J P U O O Y Q U L N Y U
Y S Q S G O S W Z M G G X Q J W M G M G A D B S G
J K H A S R A Y T E M R X P S F L D U L H D S O I
C O N S I S T F D W G X S X Z D J B A K I T X N H
X K M E N N Z V T X J C O F I T G S Y M A X U B G
H Q C P J Z P S N T H O F T D E L M O N J V A U T
T S N L W Q R I B X W M H V V S R L D K Q N O B D
E U U Q T Y O X T V Z P U N G E A A T L K I F W Q
C B H B A F G Z H U W L L H U J R X C I L S Z R T
C J S F E P R V E T A E N I Y D Y Y N V Z M D P T
X E K M E R A O O U H T T Y D V L G H P K O Y A N
K C T Q R E M Z R D M I V I N Y V F M K K X J I R
J T Y Z C E E T Y S K O M C L D P E Q R Q M T C S
A S X F X C W T Y D K N J B C K M V X F Z I P I J
C A M P U S E Z O T Z I W B N Y O W A R D D R Y V
E I L U L Z U U H Z F F X H O W A D H O K F E V E
N Z H F N C L E K J U I H J O C D V B N W B P Z A
S E R Q U W R Z F N N I T H K E D C U T E P A K Z
H P C Z B A S C R I S F G H G Q R I O R L X R N Y
X D Q T P Q I S B T L Y U R N R X D I U O T A K R
N G S Y G E N P O Y S C E D R Z K Y Z N H M T Q W
P N A D C W I R C L S E T M H J D Y G N M Y O G N
H M M T B L Y C Y B F U L C A B B L X E D F R R C
X F X Z W T E J M U S I C O L O G Y C R N F Y C U
```
