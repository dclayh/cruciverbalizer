from itertools import chain
import logging
from pathlib import Path
from tempfile import TemporaryDirectory

import requests

from cruciverbalizer.constants import LOCAL_DATA_DIR

LOGGER = logging.getLogger(__name__)

# dumps.wikimedia.org/enwiki/latest/enwiki-latest-all-titles-in-ns0.gz

def get_nyt_words(output_file):
    url_str = "https://raw.githubusercontent.com/doshea/nyt_crosswords/master/{year}/{month:02d}/{day:02d}.json"
    answer_set = set()
    for year in range(1976, 2019):
        for month in range(1, 13):
            LOGGER.info(f"Processing NYT {year}-{month}")
            for day in range(1, 32):
                response = requests.get(url_str.format(year=year, month=month, day=day))
                try:
                    answers = response.json()["answers"]
                    for answer in chain(answers["across"], answers["down"]):
                        answer_set.add(answer)
                except Exception:
                    continue
        LOGGER.info(f"Now at {len(answer_set)} unique words")
    for answer in sorted(answer_set):
        output_file.write(answer + "\n")

def main():
    nyt_file = LOCAL_DATA_DIR / "nyt.txt"
    if not nyt_file.exists():
        with open(nyt_file, "w") as f:
            get_nyt_words(f)
    #with TemporaryDirectory() as temp_dir:

