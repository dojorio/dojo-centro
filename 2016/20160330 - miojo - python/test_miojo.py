import unittest
from miojo import miojo

class TestMiojo(unittest.TestCase):
	def test_1_1(self):
		self.assertEquals(miojo(1, 1), 3) 

