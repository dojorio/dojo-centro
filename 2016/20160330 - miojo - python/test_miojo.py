import unittest
from miojo import miojo

class TestMiojo(unittest.TestCase):
	def test_1_1(self):
		self.assertEquals(miojo(1, 1), 3)

	def test_5_2(self):
		self.assertEquals(miojo(5, 2), 5)

	def test_5_1(self):
		self.assertEquals(miojo(5, 1), 3)

	def test_5_3(self):
		self.assertEquals(miojo(5, 3), 3)

	def test_3_5(self):
		self.assertEquals(miojo(3, 5), 3)

	def test_6_9(self):
		self.assertEquals(miojo(6, 9), 9)

	def test_5_7(self):
		self.assertEquals(miojo(5, 7), 10)

	def test_10_7(self):
		self.assertEquals(miojo(10, 7), 10)

	def test_7_11(self):
		self.assertEquals(miojo(7, 11), 14)

	def test_11_19(self):
		self.assertEquals(miojo(, ), 14)
	
unittest.main()