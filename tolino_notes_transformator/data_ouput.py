import json
from globals import OUTPUT_TXT, OUTPUT_JSON, OUTPUT_UNMATCHED

def print_output(word, synonyms, translations):
  print(f"Word: {word}")
  print(f"Synonyms: {synonyms}")
  print(f"Possible translations: {translations}")
  print('\n')

def generate_txt_file(word, synonyms, translations):
  with open(OUTPUT_TXT, 'a') as file:
    file.write(f"Word: {word}\n")
    file.write(f"Synonyms: {synonyms}\n")
    file.write(f"Possible translations: {translations}\n")
    file.write('\n')

def generate_txt_unmatched(word):
  with open(OUTPUT_UNMATCHED, 'a') as file:
    file.write(f"{word}\n")

def generate_json_file(data):
  if data:
    output = {
      "name": "Englisch",
      "levels": [{ "name": "Level 1", "data": data}]}

    with open(OUTPUT_JSON, 'w', encoding='utf-8') as file:
      json.dump(output, file, ensure_ascii=False, indent=2)

def generate_json_structure(question, answer, hints):
  structure = {
      "question": question,
      "answer": answer,
      "hint": hints}
  return structure