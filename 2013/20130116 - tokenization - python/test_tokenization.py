#-*- coding: utf-8 -*-
import unittest
from tokenization import tokenize

class TokenizeTestCase(unittest.TestCase):

	def test_1(self):
		self.assertEqual([('N', '1')], tokenize('1'))

	def test_2(self):
		self.assertEqual([('N', '2')], tokenize('2'))

	def test_mais(self):
		self.assertEqual([('+', '+')], tokenize('+'))

	def test_menos(self):
		self.assertEqual([('-', '-')], tokenize('-'))


unittest.main()