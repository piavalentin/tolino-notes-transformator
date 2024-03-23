"""
Processes extracted words by lemmatizing, finding synonyms, and translating them.
Depending on the configuration, a text file or a JSON file will be generated.

- Lemmatizes each extracted word.
- Finds synonyms for the lemmatized words.
- Translates the set of original and synonymous words into German.
- Depending on EXPORT_TYPE, output data to a .txt file or accumulate data for JSON.
- If GENERATE_JSON or EXPORT_TYPE is set to "json", outputs the accumulated data to a JSON file.
- Progress of processed words is displayed in the console.

Globals:
- EXPORT_TYPE (str): "txt" or "json"
- GENERATE_JSON (bool)

Uses:
- googletrans for translation.
- Custom modules for data extraction, lemmatization, synonym finding, and output formatting.

Note:
This script is the main processing pipeline, utilizing functions from imported modules.
"""

import sys
from extract_words import extracted_words
from translations import find_translations
from utils import lemmatize_word, find_synonyms
from data_ouput import generate_txt_file, generate_json_structure, generate_json_file
from globals import GENERATE_JSON, EXPORT_TYPE

data = []
data_length = len(extracted_words)
PROCESSED_DATA = 1

for word in extracted_words:
    synonyms_per_word = []
    lemmatized_word = lemmatize_word(word)
    synonyms_per_word.append(find_synonyms(lemmatized_word))
    all_words = {*synonyms_per_word[0], lemmatized_word}
    possible_translations = find_translations(all_words)

    if EXPORT_TYPE == "txt":
        generate_txt_file(
            lemmatized_word,
            ", ".join(synonyms_per_word[0]),
            ", ".join(possible_translations),
        )

    if GENERATE_JSON or EXPORT_TYPE == "json":
        data.append(
            generate_json_structure(
                lemmatized_word,
                list(possible_translations),
                ", ".join(synonyms_per_word[0]),
            )
        )

    sys.stdout.write(f"\rWords processed: {PROCESSED_DATA}/{data_length}")
    sys.stdout.flush()
    PROCESSED_DATA += 1

if GENERATE_JSON or EXPORT_TYPE == "json":
    generate_json_file(data)
