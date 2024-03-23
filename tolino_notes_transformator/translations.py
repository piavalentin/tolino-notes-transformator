from googletrans import Translator
from data_ouput import generate_txt_unmatched

def find_translations(words):
  translator = Translator()
  translations = set()

  for word in words:
    try:
      translation_result = translator.translate(word, src='en', dest='de')
      translation = translation_result.text
    except Exception as e:
      # print(f"\nError during translation for '{word}': {e}")
      translation = ""
      generate_txt_unmatched(word)
    
    if translation:
      translations.add(translation.lower())
  
  return translations