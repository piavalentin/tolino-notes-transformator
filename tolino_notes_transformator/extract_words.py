"""
This module defines functionality for extracting words from files using regex patterns.
"""

import re
from tolino_notes_transformator.globals import INPUT_FILE, PATTERN, MAX_WORDS


def extract_words(file_path, pattern, max_words):
    """
    Extracts words from a file based on a specified regex pattern and word count limit.
    Sentences extraction is planned but not yet implemented.

    Parameters:
    - file_path (str)
    - pattern (str)
    - max_words (int)

    Returns:
    - list
    """
    words = []
    sentences = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                word_count = len(match.group(1).split())
                if word_count <= max_words:
                    words.append(match.group(1).strip())
                else:
                    sentences.append(match.group(1))
    return words


extracted_words = extract_words(INPUT_FILE, PATTERN, MAX_WORDS)
