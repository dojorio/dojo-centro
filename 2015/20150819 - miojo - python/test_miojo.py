import unittest
from miojo import tempo_minimo

class TesteMiojo(unittest.TestCase):
	def test_ampulhetas_3_e_1(self):
		self.assertEqual(tempo_minimo(3,1), 3)

unittest.main()