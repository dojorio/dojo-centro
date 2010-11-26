#-*- coding: utf-8 -*-
import unittest
from espiral import *

class Teste(unittest.TestCase):

    def test_2x2(self):
        self.assertEqual(espiral(2, 2), """\
1 2
4 3""")

    def test_2x3(self):
        self.assertEqual(espiral(2, 3), """\
1 2 3
6 5 4""")
    def test_2x4(self):
        self.assertEqual(espiral(2, 4), """\
1 2 3 4
8 7 6 5""")

    def test_2x5(self):
        self.assertEqual(espiral(2, 5), """\
 1  2  3  4  5
10  9  8  7  6""")

    def test_1x1(self):
        self.assertEqual(espiral(1, 1), """\
1""")

    def test_1x2(self):
        self.assertEqual(espiral(1, 2), """\
1 2""")

if __name__ == '__main__':
    unittest.main()

