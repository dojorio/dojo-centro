import unittest
from diamante import diamante

class TestDiamante(unittest.TestCase):

	def test_A_retorna_A(self):
		result = diamante('A')

		self.assertEqual(['A'], result)

	def test_B_retorna_ABBA(self):
		expected = [
			' A ',
			'B B',
			' A ',
		]
		result = diamante('B')
		self.assertEqual(expected, result)

	def test_C_retorna_ABCCBA(self):
		expected = [
			'  A  ',
			' B B ',
			'C   C',
			' B B ',
			'  A  ',
		]
		result = diamante('C')
		self.assertEqual(expected, result)

	def test_D_retorna_ABCDDCBA(self):
		expected = [
			'   A   ',
			'  B B  ',
			' C   C ',
			'D     D',
			' C   C ',
			'  B B  ',
			'   A   ',
		]
		result = diamante('D')
		self.assertEqual(expected, result)

if __name__ == '__main__':
	unittest.main()
	print(diamante('Z'))