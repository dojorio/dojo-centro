import unittest
from codigo import ascii_art

class TestASCII(unittest.TestCase):
    def test_writes_A_in_the_left_top(self):
        self.assertEquals('A', ascii_art('0 0 65'))

    def test_writes_B_in_the_left_top(self):
        self.assertEquals('B', ascii_art('0 0 66'))

    def test_writes_D_in_the_left_top(self):
        self.assertEquals('D', ascii_art('0 0 68'))

    def test_writes_A_in_the_second_column(self):
        self.assertEquals(' A', ascii_art('0 1 65'))

    def test_writes_B_in_the_second_column(self):
        self.assertEquals(' B', ascii_art('0 1 66'))

    def test_writes_B_in_the_tenth_column(self):
        self.assertEquals('         B', ascii_art('0 9 66'))

    def test_writes_B_in_the_11th_column(self):
        self.assertEquals('          B', ascii_art('0 10 66'))

    def test_writes_C_in_the_second_row_11th_column(self):
        self.assertEquals('\n          C', ascii_art('1 10 67'))

    def test_writes_A_and_D_in_the_first_column_and_in_two_lines(self):
        self.assertEquals('A\nD', ascii_art('0 0 65\n1 0 68'))

    def test_writes_C_and_A_in_the_same_row_and_1st_and_2nd_column(self):
        self.assertEquals('A\nC', ascii_art('0 0 65\n0 1 67'))

unittest.main()

