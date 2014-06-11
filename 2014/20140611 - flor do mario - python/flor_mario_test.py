import unittest

class Test (unittest.TestCase):
	def test_parametros_iguais(self):
		self.assertTrue(demarcar([1,1,1],[1,1,1]))

if __name__ == "__main__":
	unittest.main()
