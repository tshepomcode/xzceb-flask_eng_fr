import unittest

from machinetranslation.translator import englishToFrench, frenchToEnglish

class testEnglishToFrench(unittest.TestCase):
    def test1(self):
        """
        Function tests for english to french translations
        """
        # tests when input null is given, output is Null.
        self.assertEqual(englishToFrench('null'), 'Null')
        # tests when 'Hello' input is given, output is 'Bonjour'
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

class testFrenchToEnglish(unittest.TestCase):
    def test1(self):
        """
        Function tests for French to english translations
        """
        # tests when input null is given, output is Null.
        self.assertEqual(frenchToEnglish('null'), 'Null')
         # tests when 'Bonjour' input is given, output is 'Hello'
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
unittest.main()
