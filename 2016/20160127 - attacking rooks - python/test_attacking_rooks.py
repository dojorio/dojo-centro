#https://www.urionlinejudge.com.br/judge/en/problems/view/1490
import unittest
from attacking_rooks import attacking_rooks, transpose_board

# board: integer N (1 ≤ N ≤ 100)

class TestAttackingRooks(unittest.TestCase):
	def test_1_pawn(self):
		board = [['x']]
		maximum_rooks = 0
		self.assertEquals(attacking_rooks(board), maximum_rooks)

	def test_1_empty(self):
		board = [['.']]
		maximum_rooks = 1
		self.assertEquals(attacking_rooks(board), maximum_rooks)

	def test_2x2_empty(self):
		board = [['.', '.'],
		         ['.', '.']]
		maximum_rooks = 2
		self.assertEquals(attacking_rooks(board), maximum_rooks)

	def test_2x2_1_pawn(self):
		board = [['x', '.'],
		         ['.', '.']]
		maximum_rooks = 2
		self.assertEquals(attacking_rooks(board), maximum_rooks)

	def test_2x2_2_pawns_line(self):
		board = [['x', 'x'],
		         ['.', '.']]
		maximum_rooks = 1
		self.assertEquals(attacking_rooks(board), maximum_rooks)

	def test_2x2_2_pawns_pawns_line(self):
		board = [['.', '.'],
		         ['x', 'x']]
		maximum_rooks = 1
		self.assertEquals(attacking_rooks(board), maximum_rooks)

	def test_2x2_2_pawns_column(self):
		board = [['x', '.'],
		         ['x', '.']]
		maximum_rooks = 1
		
		self.assertEquals(attacking_rooks(board), maximum_rooks)

	def test_2x2_2_pawns_diagonal(self):
		board = [['.', 'x'],
		         ['x', '.']]
		maximum_rooks = 2
		
		self.assertEquals(attacking_rooks(board), maximum_rooks)

	def test_2x2_2_pawns_diagonal_2(self):
		board = [['x', '.'],
		         ['.', 'x']]
		maximum_rooks = 2
		
		self.assertEquals(attacking_rooks(board), maximum_rooks)

	def test_3x3(self):
		board = [['.', '.', '.'],
		         ['.', '.', '.'],
		         ['.', '.', '.']]
		maximum_rooks = 3
		
		self.assertEquals(attacking_rooks(board), maximum_rooks)

	def test_3x3_central_PAU(self):
		board = [['.', '.', '.'],
		         ['.', 'x', '.'],
		         ['.', '.', '.']]
		maximum_rooks = 4
		
		self.assertEquals(attacking_rooks(board), maximum_rooks)

class TestTranspose(unittest.TestCase):
	def test_1(self):
		board = [['.']]
		self.assertEquals(transpose_board(board), board)

	def test_2(self):
		board = [['x', '.'],
		         ['x', '.']]

		transboard = [['x', 'x'],
		         	  ['.', '.']]
		
		self.assertEquals(transpose_board(board), transboard)

unittest.main()