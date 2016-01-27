#https://www.urionlinejudge.com.br/judge/en/problems/view/1490
import unittest
from attacking_rooks import attacking_rooks

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


unittest.main()