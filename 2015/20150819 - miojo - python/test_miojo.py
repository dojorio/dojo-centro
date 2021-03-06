import unittest
from miojo import tempo_minimo


class TesteMiojo(unittest.TestCase):
	def test_ampulhetas_3_e_1(self):
		self.assertEqual(tempo_minimo(3, 1), 3)

	def test_ampulhetas_5_e_2(self):
		self.assertEqual(tempo_minimo(5, 2), 5)

	def test_ampulhetas_2_e_5(self):
		self.assertEqual(tempo_minimo(2, 5), 5)

	def test_ampulhetas_1_e_3(self):
		self.assertEqual(tempo_minimo(1, 3), 3)

	def test_ampulhetas_5_e_5(self):
		self.assertIsNone(tempo_minimo(5, 5))

	def test_ampulhetas_3_e_3(self):
		self.assertEqual(tempo_minimo(3, 3), 3)

	def test_ampulhetas_1_e_1(self):
		self.assertEqual(tempo_minimo(1, 1), 3)

	def test_ampulhetas_2_e_4(self):
		self.assertIsNone(tempo_minimo(2, 4))

	def test_ampulhetas_2_e_4(self):
		self.assertIsNone(tempo_minimo(2, 4))

	def test_ampulhetas_8_e_4(self):
		self.assertIsNone(tempo_minimo(8, 4))

	def test_ampulhetas_7_e_5(self):
		self.assertEqual(tempo_minimo(7, 5), 10)

	def test_ampulhetas_11_e_7(self):
		self.assertEqual(tempo_minimo(11, 7), 14)

	def test_ampulhetas_11_e_7(self):
		self.assertEqual(tempo_minimo(11, 7), 14)

	def test_ampulhetas_7_e_2(self):
		self.assertEqual(tempo_minimo(7, 2), 7)

	def test_ampulhetas_5_e_4(self):
		self.assertEqual(tempo_minimo(5, 4), 8)

	def test_ampulhetas_7_e_6(self):
		self.assertEqual(tempo_minimo(7, 6), 21)

	def test_ampulhetas_20_e_5(self):
		self.assertIsNone(tempo_minimo(20, 5))


unittest.main()