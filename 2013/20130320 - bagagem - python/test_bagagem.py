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


unittest.main()
