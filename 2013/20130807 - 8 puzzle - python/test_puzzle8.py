# -*- coding: utf-8 -*-
import unittest
from puzzle8 import resolver

class TestPuzzle8(unittest.TestCase):
	def test_ja_ordenado(self):
		tabuleiro = '12345678x'
		movimentos = ''
		self.assertEqual(movimentos, resolver(tabuleiro))

	def test_6_uma_casa_para_baixo(self):
		tabuleiro = '12345x786'
		movimentos = '6'
		self.assertEqual(movimentos, resolver(tabuleiro))

	def test_8_uma_casa_a_direita(self):
		tabuleiro = '1234567x8'
		movimentos = '8'
		self.assertEqual(movimentos, resolver(tabuleiro))

	def test_x_na_terceira_casa(self):
		tabuleiro = '12x453786'
		movimentos = '36'
		self.assertEqual(movimentos, resolver(tabuleiro))

	def test_x_na_setima_casa(self):
		tabuleiro = '123456x78'
		movimentos = '78'
		self.assertEqual(movimentos, resolver(tabuleiro))

	def test_x_na_quarta_casa_e_dando_a_volta(self):
		tabuleiro = '412x53786'
		movimentos = '41236'
		self.assertEqual(movimentos, resolver(tabuleiro))

	def test_1234857x6(self):
		tabuleiro = '1234857x6'
		movimentos = '856'
		self.assertEqual(movimentos, resolver(tabuleiro))

	def test_412753x86(self):
		tabuleiro = '412753x86'
		movimentos = '741236'
		self.assertEqual(movimentos, resolver(tabuleiro))

	def test_1238x5476_passinho_do_volante(self):
		tabuleiro = '1238x5476'
		movimentos = '847856'
		self.assertEqual(movimentos, resolver(tabuleiro))



unittest.main()
