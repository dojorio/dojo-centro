import unittest
from matriz import espiral

class TestMatriz(unittest.TestCase):
	def test_1_x_1(self):
		self.assertEqual(espiral(1, 1), [[1]])

	def test_2_x_1(self):
		self.assertEqual(espiral(2, 1), [[1,2]])

	def test_3_x_1(self):
		self.assertEqual(espiral(3, 1), [[1,2,3]])

	def test_4_x_1(self):
		self.assertEqual(espiral(4, 1), [[1,2,3,4]])

	def test_1_x_2(self):
		self.assertEqual(espiral(1, 2), [[1],[2]])

	def test_2_x_2(self):
		self.assertEqual(espiral(2, 2), [[1,2],[4,3]])

	def test_1_x_3(self):
		self.assertEqual(espiral(1, 3), [[1], [2], [3]])

	def test_1_x_4(self):
		self.assertEqual(espiral(1, 4), [[1], [2], [3], [4]])

	def test_2_x_3(self):
		self.assertEqual(espiral(2, 3), [[1,2], [6,3], [5,4]])



unittest.main()
