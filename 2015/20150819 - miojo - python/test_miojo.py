import unittest
from miojo import tempo_minimo

class TesteMiojo(unittest.TestCase):
	def test_ampulhetas_3_e_1(self):
		self.assertEqual(tempo_minimo(3,1), 3)

	def test_ampulhetas_5_e_2(self):
		self.assertEqual(tempo_minimo(5,2), 5)

	def test_ampulhetas_2_e_5(self):
		self.assertEqual(tempo_minimo(2,5), 5)
unittest.main()