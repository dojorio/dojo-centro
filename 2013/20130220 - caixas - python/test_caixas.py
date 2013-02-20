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



unittest.main()