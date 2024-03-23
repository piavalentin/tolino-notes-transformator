"""
Utilizes the Google Translate API to translate English words to German and logs any 
untranslatable words. This module encapsulates the translation process and error handling.
"""

from googletrans import Translator
from data_ouput import generate_txt_unmatched


def find_translations(words):
    """
    Translates a list of English words into German using the Google Translate API.
    Untranslatable words are logged to a separate file.

    Parameters:
    - words (list)

    Returns:
    - set

    Notes:
    - Relies on googletrans library
    - Errors in translation are handled silently, logging unmatched words
    """
    translator = Translator()
    translations = set()

    for word in words:
        try:
            translation_result = translator.translate(word, src="en", dest="de")
            translation = translation_result.text
        # pylint: disable=broad-except
        except Exception:
            translation = ""
            generate_txt_unmatched(word)

        if translation:
            translations.add(translation.lower())

    return translations
