import unittest
from wordwrap import WordWrapper


class WordWrapperTest(unittest.TestCase):
    def test_wrap_empty_string(self):
        self.assertEqual(WordWrapper(80).wrap(""), "")

    def test_wrap_single_word_that_fits_into_line(self):
        self.assertEqual(WordWrapper(80).wrap("Juan"), "Juan")

    def test_wrap_two_words_that_fit(self):
        self.assertEqual(WordWrapper(80).wrap("casa rato"), "casa rato")

    def test_wrap_two_words_that_doesnt_fit(self):
        self.assertEqual(WordWrapper(5).wrap("casa rato"), "casa\nrato")
        
    def test_wrap_single_word_that_doesn_fit_into_line(self):
        self.assertEqual(WordWrapper(2).wrap("casa"), "ca\nsa")

    def test_wrap_single_word_that_doesn_fit_into_line_breaking_multiple_times(self):
        self.assertEqual(WordWrapper(1).wrap("casa"), "c\na\ns\na")
        
    def test_wrap_two_words_that_doesnt_fit_into_six_cols(self):
        self.assertEqual(WordWrapper(9).wrap("  texto indentado"), "  texto\nindentado")

        
unittest.main()
