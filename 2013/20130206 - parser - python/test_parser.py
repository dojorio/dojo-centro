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

	def test_one_binary_operator_plus(self):
		tokens = [('N', '2'),('+', '+'),('N', '2')]
		expected = ('+', 2, 2)
		self.assertEqual(expected, parse(tokens))

	def test_one_binary_operator_minus(self):
		tokens = [('N', '2'),('-', '-'),('N', '2')]
		expected = ('-', 2, 2)
		self.assertEqual(expected, parse(tokens))


	def test_one_binary_operator_times(self):
		tokens = [('N', '2'),('*', '*'),('N', '2')]
		expected = ('*', 2, 2)
		self.assertEqual(expected, parse(tokens))

	def test_one_binary_operator_times_3_3(self):
		tokens = [('N', '3'),('*', '*'),('N', '3')]
		expected = ('*', 3, 3)
		self.assertEqual(expected, parse(tokens))

	def test_two_binary_operators_plus(self):
		tokens = [('N', '2'),('+', '+'),('N', '3'),('+', '+'),('N', '4')]
		expected = ('+', ('+', 2, 3), 4)
		self.assertEqual(expected, parse(tokens))

	def test_two_binary_operators_plus_minus(self):
		tokens = [('N', '1'),('+', '+'),('N', '2'),('-', '-'),('N', '3')]
		expected = ('-', ('+', 1, 2), 3)
		self.assertEqual(expected, parse(tokens))

	def test_two_binary_operators_plus_2(self):
		tokens = [('N', '3'),('+', '+'),('N', '4'),('+', '+'),('N', '5')]
		expected = ('+', ('+', 3, 4), 5)
		self.assertEqual(expected, parse(tokens))

	def test_two_binary_operators_4_plus_2_times_3(self):
		tokens = [('N', '4'),('+', '+'),('N', '2'),('*', '*'),('N', '3')]
		expected = ('+', 4, ('*', 2, 3))
		self.assertEqual(expected, parse(tokens))



unittest.main()