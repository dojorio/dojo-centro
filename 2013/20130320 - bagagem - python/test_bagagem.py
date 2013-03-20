#-*- coding: utf-8 -*-
import unittest
from bagagem import divisivel

class BagagemTestCase(unittest.TestCase):

	def test_nenhuma_mala(self):
		malas = []
		self.assertTrue(divisivel(malas))

	def test_uma_mala(self):
		malas = [7]
		self.assertFalse(divisivel(malas))

	def test_duas_malas_iguais(self):
		malas = [7, 7]
		self.assertTrue(divisivel(malas))

	def test_duas_malas_diferentes(self):
		malas = [5, 7]
		self.assertFalse(divisivel(malas))

	def test_tres_malas_divisiveis(self):
		malas = [7, 5, 2]
		self.assertTrue(divisivel(malas))

	def test_tres_malas_divisiveis_invertido(self):
		malas = [5, 2, 7]
		self.assertTrue(divisivel(malas))

	def test_tres_malas_nao_divisiveis(self):
		malas = [7, 7, 1]
		self.assertFalse(divisivel(malas))

	def test_tres_malas_divisiveis_misturada(self):
		malas = [3, 7, 4]
		self.assertTrue(divisivel(malas))

	def test_tres_malas_nao_divisiveis_misturada(self):
		malas = [2, 7, 4]
		self.assertFalse(divisivel(malas))

	def test_tres_malas_nao_divisiveis_iguais(self):
		malas = [7, 7, 7]
		self.assertFalse(divisivel(malas))

	def test_quatro_malas_divisiveis(self):
		malas = [3,3,3,3]
		self.assertTrue(divisivel(malas))



unittest.main()
