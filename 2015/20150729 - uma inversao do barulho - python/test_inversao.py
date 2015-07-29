import unittest
from inversao import inverte_um

class TestInversao(unittest.TestCase):
	def test_0_0(self):
		self.assertEquals(inverte_um([0, 0]), [1, 0])

	def test_0_1(self):
		self.assertEquals(inverte_um([0, 1]), [1, 1])

	def test_1_0(self):
		self.assertEquals(inverte_um([1, 0]), [1, 1])	

unittest.main()