import unittest
from espiral import *

class TestEspiral(unittest.TestCase):
	def test_espiral_1_por_1(self):
		self.assertEqual([[1]], espiral(1, 1))

	def test_espiral_2_por_1(self):
		self.assertEqual([[1, 2]], espiral(2, 1))

	def test_espiral_3_por_1(self):
		self.assertEqual([[1, 2, 3]], espiral(3, 1))

	def test_espiral_4_por_1(self):
		self.assertEqual([[1, 2, 3, 4]], espiral(4, 1))

	def test_espiral_1_por_2(self):
		self.assertEqual([[1],[2]], espiral(1, 2))

	def test_espiral_1_por_3(self):
		self.assertEqual([[1],[2],[3]], espiral(1, 3))

	def test_espiral_1_por_4(self):
		self.assertEqual([[1],[2],[3],[4]], espiral(1, 4))

	def test_espiral_2_por_2(self):
		self.assertEqual([[1, 2],[4, 3]], espiral(2, 2))

	def test_espiral_3_por_2(self):
		self.assertEqual([[1, 2, 3],[6, 5, 4]], espiral(3, 2))

	def _test_espiral_2_por_3(self):
		self.assertEqual([[1, 2],[6, 3],[5, 4]], espiral(2, 3))

class TestPCZ(unittest.TestCase):
	def test_matriz_zerada_de_ordem_1(self):
		self.assertEqual([[0]], preencher_com_zeros(1, 1))

	def test_matriz_zerada_de_indice_2_1(self):
		self.assertEqual([[0 , 0]], preencher_com_zeros(2, 1))

	def test_matriz_zerada_de_indice_2_2(self):
		self.assertEqual([[0 , 0],[0 , 0]], preencher_com_zeros(2, 2))

	def test_matriz_zerada_de_indice_3_2(self):
		self.assertEqual([[0 , 0, 0],[0 , 0, 0]], preencher_com_zeros(3, 2))

unittest.main()


