#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_1_row(self):
        self.assertEqual(pascal_triangle(1), [[1]])

    def test_2_row(self):
        self.assertEqual(pascal_triangle(2), [[1], [1, 1]])

    def test_3_row(self):
        self.assertEqual(pascal_triangle(3), [[1], [1, 1], [1, 2, 1]])


if __name__ == "__main__":
    unittest.main()

