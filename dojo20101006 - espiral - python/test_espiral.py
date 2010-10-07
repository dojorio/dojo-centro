#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from espiral import *


class TesteEspiral(unittest.TestCase):
    def test_espiral_1_por_1(self):
        self.assertEqual(espiral(1, 1), '1')

    def test_espiral_1_por_2(self):
        self.assertEqual(espiral(1, 2), '1 2')

    def test_espiral_1_por_3(self):
        self.assertEqual(espiral(1, 3), '1 2 3')

    def test_espiral_2_por_1(self):
        self.assertEqual(espiral(2, 1), '''\
1
2''')

    def test_espiral_2_por_2(self):
        self.assertEqual(espiral(2, 2), '''\
1 2
4 3''')

    def test_espiral_2_por_5(self):
        self.assertEqual(espiral(2, 5), '''\
 1  2  3  4  5
10  9  8  7  6''')

if __name__ == "__main__":
    unittest.main()

