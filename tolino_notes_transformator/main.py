import sys
from extract_words import extracted_words
from translations import find_translations
from utils import lemmatize_word, find_synonyms
from data_ouput import generate_txt_file, generate_json_structure, generate_json_file
from globals import GENERATE_JSON, EXPORT_TYPE

data = []
data_length = len(extracted_words)
processed_data = 1

for word in extracted_words:
    synonyms_per_word = []
    lemmatized_word = lemmatize_word(word)
    synonyms_per_word.append(find_synonyms(lemmatized_word))
    all_words = {*synonyms_per_word[0], lemmatized_word}
    possible_translations = find_translations(all_words)

    if EXPORT_TYPE == 'txt':
      generate_txt_file(
          lemmatized_word,
          ', '.join(synonyms_per_word[0]),
          ', '.join(possible_translations))

    if GENERATE_JSON or EXPORT_TYPE == 'json':
      data.append(generate_json_structure(
          lemmatized_word,
          list(possible_translations),
          ', '.join(synonyms_per_word[0])))
    
    sys.stdout.write(f"\rWords processed: {processed_data}/{data_length}")
    sys.stdout.flush()
    processed_data += 1

if GENERATE_JSON or EXPORT_TYPE == 'json':
    generate_json_file(data)