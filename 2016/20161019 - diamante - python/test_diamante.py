import unittest
from diamante import diamante

class TestDiamante(unittest.TestCase):

	def test_A_retorna_A(self):
		result = diamante('A')

		self.assertEqual([['A']], result)

	def test_B_retorna_ABBA(self):
		expected = [
			[' ', 'A', ' '],
			['B', ' ', 'B'],
			[' ', 'A', ' ']
		]
		result = diamante('B')
		self.assertEqual(expected, result)
if __name__ == '__main__':
	unittest.main()