import unittest
from knight import move

class TestKnight(unittest.TestCase):
    def test_no_moves(self):
        self.assertEqual(move(1, 1, 1, 1), 0)

    def test_one_move(self):
        self.assertEqual(move(1, 1, 2, 3), 1)

    def test_two_moves(self):
        self.assertEqual(move(1, 1, 3, 5), 2)
        self.assertEqual(move(1, 1, 1, 5), 2)

    def test_three_moves(self):
        self.assertEqual(move(1, 1, 1, 2), 3)
        self.assertEqual(move(2, 1, 1, 1), 3)

    def test_four_moves(self):
        self.assertEqual(move(1, 1, 1, 3), 2)
   
    def test_one_diagonal_move(self):
        self.assertEqual(move(1, 1, 2, 2), 4)
   
unittest.main()
