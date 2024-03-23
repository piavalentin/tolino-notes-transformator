import nltk
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

from globals import MAX_SYNONYMS

def lemmatize_word(word):
  lemmatizer = WordNetLemmatizer()

  if word.endswith('ing'):
    return word

  return lemmatizer.lemmatize(word, pos='v')

def is_different_to_synonym(word, synonym):
  return word.lower() != synonym.lower()

def find_synonyms(word):
  count = 0 # TODO check for 0 as unlimited
  synonyms = set()
  
  for synonym in wordnet.synsets(word):
    for lemma in synonym.lemmas():
      synonym = lemma.name()

      if is_different_to_synonym(word, synonym) and MAX_SYNONYMS != 0 and count <= MAX_SYNONYMS:
          synonyms.add(synonym.replace("_", " "))
          count += 1
  return synonyms