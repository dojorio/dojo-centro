# -*- coding: utf-8 -*-

import unittest
from skyline import skyline

class TestSkyline(unittest.TestCase):
	def test_no_buildings(self):
		saida = skyline([])
		esperado = []
		self.assertEqual(esperado, saida)

	def test_one_building(self):
		saida = skyline([(0, 1, 1)])
		esperado = [(0,1), (1, 0)]
		self.assertEqual(esperado, saida)

	def teste_um_predio_mais_pra_direita(self):
		saida = skyline([(1, 1, 2)])
		esperado = [(1,1), (2, 0)]
		self.assertEqual(esperado, saida)

	def teste_um_predio_mais_pra_direita_largura10(self):
		saida = skyline([(5, 14, 15)])
		esperado = [(5,14), (15, 0)]
		self.assertEqual(esperado, saida)

	def teste_2_predio_colado_com_alturas_diferentes(self):
		saida = skyline([(0, 1, 1), (1, 2, 2)])
		esperado = [(0, 1), (1, 2), (2, 0)]
		self.assertEqual(esperado, saida)

	def teste_2_predio_colado_com_alturas_diferentes_mais_largo(self):
		saida = skyline([(0, 1, 1), (1, 2, 3)])
		esperado = [(0, 1), (1, 2), (3, 0)]
		self.assertEqual(esperado, saida)

	def teste_2_predio_colado_com_alturas_iguais(self):
		saida = skyline([(0, 1, 1), (1, 1, 2)])
		esperado = [(0, 1), (2, 0)]
		self.assertEqual(esperado, saida)



unittest.main()


