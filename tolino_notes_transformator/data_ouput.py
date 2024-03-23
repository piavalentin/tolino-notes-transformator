"""
Facilitates output generation in both text and JSON formats for word processing results, including
word translations and synonyms. Functions are provided to print outputs to the console, append them 
to text files, and generate structured JSON files. Supports handling unmatched words.
"""

import json
from tolino_notes_transformator.globals import OUTPUT_TXT, OUTPUT_JSON, OUTPUT_UNMATCHED


def print_output(word, synonyms, translations):
    """
    Prints the word, its synonyms, and possible translations.

    Parameters:
    - word (str)
    - synonyms (list)
    - translations (list)

    Returns:
    - None
    """
    print(f"Word: {word}")
    print(f"Synonyms: {synonyms}")
    print(f"Possible translations: {translations}")
    print("\n")


def generate_txt_file(word, synonyms, translations):
    """
    Appends a word, its synonyms, and translations to a specified text file.

    Parameters:
    - word (str)
    - synonyms (list)
    - translations (list)

    Returns:
    - None
    """
    with open(OUTPUT_TXT, "a", encoding="utf-8") as file:
        file.write(f"Word: {word}\n")
        file.write(f"Synonyms: {synonyms}\n")
        file.write(f"Possible translations: {translations}\n")
        file.write("\n")


def generate_txt_unmatched(word):
    """
    Appends unmatched words to a specified text file for further review.

    Parameters:
    - word (str)

    Returns:
    - None
    """
    with open(OUTPUT_UNMATCHED, "a", encoding="utf-8") as file:
        file.write(f"{word}\n")


def generate_json_file(data):
    """
    Writes provided data into a JSON file with a specific structure.

    Parameters:
    - data (list)

    Returns:
    - None
    """
    if data:
        output = {"name": "Englisch", "levels": [{"name": "Level 1", "data": data}]}

        with open(OUTPUT_JSON, "w", encoding="utf-8") as file:
            json.dump(output, file, ensure_ascii=False, indent=2)


def generate_json_structure(question, answer, hints):
    """
    Constructs a dictionary structure for a question-answer-hint set.

    Parameters:
    - question (str)
    - answer (list)
    - hints (str)

    Returns:
    - dict
    """
    structure = {"question": question, "answer": answer, "hint": hints}
    return structure
