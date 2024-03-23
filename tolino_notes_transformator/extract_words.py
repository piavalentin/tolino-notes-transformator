import re
from globals import INPUT_FILE, PATTERN, MAX_WORDS

def extract_words(file_path, pattern, max_words):
  words = []
  sentences = []
  with open(file_path, 'r', encoding='utf-8') as file:
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