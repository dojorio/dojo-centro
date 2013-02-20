#-*- coding: utf-8 -*-
import unittest
from caixas import empilhar

class CaixasTestCase(unittest.TestCase):

	def test_nenhuma_caixa(self):
		caixas = []
		resultado = empilhar(caixas)
		self.assertEquals(0, resultado)

	def test_uma_caixa(self):
		caixas = [(1, 1)]
		resultado = empilhar(caixas)
		self.assertEquals(1, resultado)

	def test_duas_caixas(self):
		caixas = [(2, 1), (2, 1)]
		self.assertEquals(1, empilhar(caixas))

	def test_duas_caixas_que_empilham(self):
		caixas = [(2, 1), (1, 1)]
		self.assertEquals(2, empilhar(caixas))

unittest.main()