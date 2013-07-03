import unittest
from street import directions

class TestStreet(unittest.TestCase):

	def test_1_2_returns_0(self):
		entrada = [(1, 2)]
		self.assertEqual(0, directions(entrada))

	def test_cycle_size_3_returns_3(self):
		entrada = [(1, 2), (2, 3), (3, 1)]
		self.assertEqual(3, directions(entrada))

	def test_1_2_2_3_3_1_3_4_returns_3(self):
		entrada = [(1, 2), (2, 3), (3, 1), (3, 4)]
		self.assertEqual(3, directions(entrada))

	def test_cycle_size_4_returns_4(self):
		entrada = [(1, 2), (2, 3), (3, 4), (4, 1)]
		self.assertEqual(4, directions(entrada))

	def test_cycle_size_5_returns_5(self):
		entrada = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]
		self.assertEqual(5, directions(entrada))

	def test_2_cycles_size_3_connected_by_a_street_returns_6(self):
		entrada = [(1, 2), (2, 3), (3, 1), (3, 4), (4, 5), (5, 6), (6, 4)]
		self.assertEqual(6, directions(entrada))

	def test_1_cycles_size_4_with_diagonal_returns_5(self):
		entrada = [(1, 2), (2, 3), (3, 4), (4, 1), (2, 4)]
		self.assertEqual(5, directions(entrada))


unittest.main()


