import unittest
from inversao import inverte_um

"""
0 1 0
1 1 0 <- fica o que tem mais 1 no lado esquerdo
0 1 1
"""
class TestInversao(unittest.TestCase):
	def test_0_0(self):
		self.assertEquals(inverte_um([0, 0]), [1, 0])

	def test_0_1(self):
		self.assertEquals(inverte_um([0, 1]), [1, 1])

	def test_1_0(self):
		self.assertEquals(inverte_um([1, 0]), [1, 1])	

	def test_0_0_0(self):
		self.assertEquals(inverte_um([0, 0, 0]), [1, 0, 0])

	def test_0_1_0(self):
		self.assertEquals(inverte_um([0, 1, 0]), [1, 1, 0])

	def test_1_0_0(self):
		self.assertEquals(inverte_um([1, 0, 0]), [1, 1, 0])

	def test_0_0_1(self):
		self.assertEquals(inverte_um([0, 0, 1]), [1, 0, 1])

	def test_1_0_0_1_1(self):
		self.assertEquals(inverte_um([1, 0, 0, 1, 1]), [1, 1, 0, 1, 1])

unittest.main()