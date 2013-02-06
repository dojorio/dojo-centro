#-*- coding: utf-8 -*-
import unittest
from parser import parse

class ParserTestCase(unittest.TestCase):
	# entrada = [('N', '5'), ('+', '+'), ('N', '5')]
	# saida = ('+', 5, 5)

	def test_one_token(self):
		tokens = [('N', '42')]
		expected = 42
		self.assertEqual(expected, parse(tokens))

	def test_one_token_2(self):
		tokens = [('N', '2')]
		expected = 2
		self.assertEqual(expected, parse(tokens))

unittest.main()