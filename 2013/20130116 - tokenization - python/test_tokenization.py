#-*- coding: utf-8 -*-
import unittest
from tokenization import tokenize, UnknownTokenException, parse

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

	def test_operador_desconhecido(self):
		with self.assertRaises(UnknownTokenException) as e:
			tokenize('1,1')

		self.assertEqual(e.exception.message, 1)

	def test_para_os_operadores_validos(self):
		self.assertEqual([
			('+', '+'),
			('-', '-'),
			('*', '*'),
			('/', '/'),
			(':', ':'),
			('(', '('),
			(')', ')'),
		], tokenize('+-*/:()'))

class ParseTestCase(unittest.TestCase):
	def test_1(self):
		self.assertEqual([1], parse(tokenize('1')))

	def test_2(self):
		self.assertEqual([2], parse(tokenize('2')))

	def test_1_mais_1(self):
		self.assertEqual([1,1,'+'], parse(tokenize('1+1')))

	def test_2_mais_2(self):
		self.assertEqual([2,2,'+'], parse(tokenize('2+2')))

	def test_2_mais_2_mais_1(self):
		self.assertEqual([2,2,'+',1,'+'], parse(tokenize('2+2+1')))

unittest.main()

