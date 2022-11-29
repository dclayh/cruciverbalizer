import re
import sys

from cruciverbalizer.constants import LOCAL_DATA_DIR


def load_wordlists():
    master_wordlist = []
    for wordfile in LOCAL_DATA_DIR.iterdir():
        master_wordlist.extend(open(wordfile).read().splitlines())
    print(f"Loaded {len(master_wordlist)} words.")
    return master_wordlist


def main():
    word_str = sys.argv[1]
    word_re = re.compile(word_str, re.IGNORECASE)
    wordlist = load_wordlists()
    for word in wordlist:
        if word_re.fullmatch(word):
            print(word)