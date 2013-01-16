#-*- coding: utf-8 -*-
import unittest
from tokenization import tokenize

class TokenizeTestCase(unittest.TestCase):

	def test_1(self):
		self.assertEqual([('N', '1')], tokenize('1'))

	def test_2(self):
		self.assertEqual([('N', '2')], tokenize('2'))

	def test_11(self):
		self.assertEqual([('N', '11')], tokenize('11'))

	def test_mais(self):
		self.assertEqual([('+', '+')], tokenize('+'))

	def test_menos(self):
		self.assertEqual([('-', '-')], tokenize('-'))

	def test_1_mais_1(self):
		self.assertEqual([
			('N', '1'),
			('+', '+'),
			('N', '1')
		], tokenize('1+1'))

	def test_1_mais_1_com_espacos(self):
		self.assertEqual([
			('N', '1'),
			('+', '+'),
			('N', '1')
		], tokenize('1 + 1'))

	def test_1_espaco_1(self):
		self.assertEqual([
			('N', '1'),
			('N', '1')
		], tokenize('1 1'))

	def test_11_mais_11(self):
		self.assertEqual([
			('N', '11'),
			('+', '+'),
			('N', '11')
		], tokenize('11+11'))

	def test_1_mais_2_menos_3(self):
		self.assertEqual([
			('N', '1'),
			('+', '+'),
			('N', '2'),
			('-', '-'),
			('N', '3')
		], tokenize('1+2-3'))


unittest.main()
