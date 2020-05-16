import bejeweled
import unittest

class TestBejeweled(unittest.TestCase):

    def test_board_have_3_adjacent_numbers_begining_row(self):
        board = ['11112452',
                 '12331532',
                 '23426723',
                 '11212452',
                 '12331532',
                 '23426723',
                 '23426723',
                 '11212452']
        self.assertTrue(bejeweled.explode(board))

    def test_board_have_3_adjacent_numbers(self):
        board = ['21112452',
                 '12331532',
                 '23426723',
                 '11212452',
                 '12331532',
                 '23426723',
                 '23426723',
                 '11212452']
        self.assertTrue(bejeweled.explode(board))

    def test_board_have_3_adjacent_numbers(self):
        board = ['21112452',
                 '12331532',
                 '23426723',
                 '11212452',
                 '12331532',
                 '23426723',
                 '23426723',
                 '11212452']
        self.assertTrue(bejeweled.explode(board))

    def test_board_have_3_adjacent_numbers_another_row(self):
        board = ['12331532',
                 '21112452',
                 '23426723',
                 '11212452',
                 '12331532',
                 '23426723',
                 '23426723',
                 '11212452']
        self.assertTrue(bejeweled.explode(board))

    def test_board_have_3_same_adjacent_numbers_2(self):
        board = ['11222452',
                 '12331532',
                 '23426723',
                 '11212452',
                 '12331532',
                 '23426723',
                 '23426723',
                 '11212452']
        self.assertTrue(bejeweled.explode(board))

    def test_board_does_not_have_3_same_adjacent_numbers(self):
        board = ['11212452',
                 '12331532',
                 '23426723',
                 '11212452',
                 '12331532',
                 '23426723',
                 '23426723',
                 '11212452']
        self.assertFalse(bejeweled.explode(board))

    def test_board_does_have_3_same_adjacent_numbers_in_a_column(self):
        board = ['11212452',
                 '12331532',
                 '13426723',
                 '11212452',
                 '12331532',
                 '23426723',
                 '23426723',
                 '11212452']
        self.assertTrue(bejeweled.explode(board))

    def test_board_have_3_same_adjacent_numbers_in_column_2(self):
        board = ['11212452',
                 '12331532',
                 '22426723',
                 '12212452',
                 '12331532',
                 '23426723',
                 '23426723',
                 '11212452']
        self.assertTrue(bejeweled.explode(board))

    def test_board_have_3adjacent_numbers_in_3_row(self):
        board = ['11212452',
                 '12331532',
                 '22226723',
                 '11212452',
                 '12331532',
                 '23426723',
                 '23426723',
                 '11212452']
        self.assertTrue(bejeweled.explode(board))



if __name__ == '__main__':
    unittest.main()