import unittest

from minesweeper import *

class MineSweeperTest(unittest.TestCase):
    def test_one_mine_1x1(self):
        field = '*'
        self.assertEqual(solve(field), '*')

    def test_one_mine_2x1(self):
        field = '*.'
        self.assertEqual(solve(field), '*1')
    
    def test_two_mines_2x1(self):
        field = '**'
        self.assertEqual(solve(field), '**')
 
    def test_one_mine_2x2(self):
        field = (
                '*.\n'
                '..'
                )
        result = (
                '*1\n'
                '11'
                )
        self.assertEqual(solve(field), result)

    def test_two_mines_2x2(self):
        field = (
                '*.\n'
                '.*'
                )
        result = (
                '*2\n'
                '2*'
                )
        self.assertEqual(solve(field), result)

    def test_three_mines_2x2(self):
        field = (
                '**\n'
                '.*'
                )
        result = (
                '**\n'
                '3*'
                )
        self.assertEqual(solve(field), result)

    def not_test_one_mine_3x2(self):
        field = (
                '*..\n'
                '...'
                )
        result = (
                '*10\n'
                '110'
                )
        self.assertEqual(solve(field), result)

    def test_two_mines_6x1(self):
        field = (
                '*..*..'
                )
        result = (
                '*11*10'
                )
        self.assertEqual(solve(field), result)

    def test_two_mines_6x1_reloaded(self):
        field = (
                '.*..*.'
                )
        result = (
                '1*11*1'
                )
        self.assertEqual(solve(field), result)

        

if __name__ == '__main__':
    unittest.main()
