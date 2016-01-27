#https://www.urionlinejudge.com.br/judge/en/problems/view/1490
import unittest
from attacking_rooks import attacking_rooks

class TestAttackingRooks(unittest.TestCase):
	def test_1_pawn(self):
		board = [['x']]
		maximum_rooks = 0
		self.assertEquals(attacking_rooks(board), maximum_rooks)

	def test_1_empty(self):
		board = [['.']]
		maximum_rooks = 1
		self.assertEquals(attacking_rooks(board), maximum_rooks)

unittest.main()