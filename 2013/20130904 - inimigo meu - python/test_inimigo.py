# -*- coding: utf-8 -*-
import unittest
from inimigo import Guerra

class TestInimigo(unittest.TestCase):
	def assertLados(self, guerra, ladoA, ladoB):
		lados = guerra.lados()
		self.assertIn(ladoA, lados)
		self.assertIn(ladoB, lados)

	def test_dois_paises(self):
		guerra = Guerra()
		guerra.sao_inimigos('A', 'B')
		self.assertLados(guerra, {'A'}, {'B'})

	def test_dois_paises2(self):
		guerra = Guerra()
		guerra.sao_inimigos('A', 'C')
		self.assertLados(guerra, {'A'}, {'C'})

	def test_dois_paises_amigos(self):
		guerra = Guerra()
		guerra.sao_amigos('A', 'C')
		self.assertLados(guerra, {'A', 'C'}, set())

	def test_tres_paises(self):
		guerra = Guerra()
		guerra.sao_inimigos('A','B')
		guerra.sao_amigos('A', 'C')
		self.assertLados(guerra, {'A', 'C'}, {'B'})

	def test_tres_paises2(self):
		guerra = Guerra()
		guerra.sao_inimigos('A','C')
		guerra.sao_amigos('A', 'B')
		self.assertLados(guerra, {'A', 'B'}, {'C'})

	def test_tres_paises3(self):
		guerra = Guerra()
		guerra.sao_inimigos('A','C')
		guerra.sao_inimigos('B', 'A')
		self.assertLados(guerra, {'B','C'}, {'A'})

	def test_tres_paises4(self):
		guerra = Guerra()
		guerra.sao_inimigos('B','A')
		guerra.sao_amigos('A','C')
		self.assertLados(guerra, {'A','C'}, {'B'})

	def test_quatro_paises(self):
		guerra = Guerra()
		guerra.sao_amigos('A','B')
		guerra.sao_amigos('C','D')
		guerra.sao_inimigos('C','A')
		self.assertLados(guerra, {'A','B'}, {'C', 'D'})


unittest.main()
