"""
Testing translation lookup
"""
import unittest
from unittest.mock import patch
from tolino_notes_transformator.translations import find_translations


# pylint: disable=missing-class-docstring
class TestFindTranslations(unittest.TestCase):
    @patch("googletrans.Translator.translate")
    # pylint: disable=missing-function-docstring
    def test_translation(self, mock_translate):
        mock_translate.return_value.text = "World"
        self.assertEqual(find_translations(["welt"]), {"world"})
