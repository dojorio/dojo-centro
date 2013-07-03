import unittest
from street import directions

class TestStreet(unittest.TestCase):

	def test_1_2_returns_0(self):
		entrada = [(1, 2)]
		self.assertEqual(0, directions(entrada))

	def test_1_2_2_3_3_1_returns_3(self):
		entrada = [(1, 2), (2, 3), (3, 1)]
		self.assertEqual(3, directions(entrada))

unittest.main()


