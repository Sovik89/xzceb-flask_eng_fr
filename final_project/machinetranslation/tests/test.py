import unittest
from ..translator.py import english_to_french,french_to_english

class TestTranslator(unittest.TestCase):
    def test1(self):
        """
        Test for English to french and French to English
        """
        self.assertEqual(english_to_french("Hello"),'Bonjour')
        self.assertEqual(french_to_english("Bonjour"),'Hello')
    

    def test2(self):
        """
        Null value passing to both the function
        """
        self.assertEqual(english_to_french(),None)
        self.assertEqual(french_to_english(),None)


unittest.main()