"""
Provides utility functions for text processing including word lemmatization and synonym finding
using NLTK's WordNet. It supports filtering synonyms up to a specified limit set by MAX_SYNONYMS
and includes functionality to specifically handle words ending in 'ing'.
"""

import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from tolino_notes_transformator.globals import MAX_SYNONYMS

nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)


def lemmatize_word(word):
    """
    Lemmatizes a word, preserving words ending in 'ing'.

    Parameters:
    - word (str)

    Returns:
    - str
    """
    lemmatizer = WordNetLemmatizer()

    if word.endswith("ing"):
        return word

    return lemmatizer.lemmatize(word, pos="v")


def is_different_to_synonym(word, synonym):
    """
    Checks if a word differs from a potential synonym, case-insensitively.

    Parameters:
    - word (str)
    - synonym (str)

    Returns:
    - bool
    """
    return word.lower() != synonym.lower()


def find_synonyms(word):
    """
    Finds up to MAX_SYNONYMS unique synonyms for a word, excluding the word itself.

    Parameters:
    - word (str)

    Returns:
    - set

    Note:
    - MAX_SYNONYMS is used to limit the number of synonyms.
    - If 0, the limit is 'unlimited' (to be implemented)
    """
    count = 0
    synonyms = set()

    for synonym in wordnet.synsets(word):
        for lemma in synonym.lemmas():
            synonym = lemma.name()

            if (
                is_different_to_synonym(word, synonym)
                and MAX_SYNONYMS != 0
                and count <= MAX_SYNONYMS
            ):
                synonyms.add(synonym.replace("_", " "))
                count += 1
    return synonyms
