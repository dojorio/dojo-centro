import unittest
from espiral import espiral

class TestEspiral(unittest.TestCase):
	def test_espiral_1_por_1(self):
		self.assertEqual([[1]], espiral(1, 1))

	def test_espiral_2_por_1(self):
		self.assertEqual([[1, 2]], espiral(2, 1))

	def test_espiral_3_por_1(self):
		self.assertEqual([[1, 2, 3]], espiral(3, 1))

	def test_espiral_4_por_1(self):
		self.assertEqual([[1, 2, 3, 4]], espiral(4, 1))

unittest.main()


