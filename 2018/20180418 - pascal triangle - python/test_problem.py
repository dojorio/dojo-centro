#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_1_row(self):
        self.assertEqual(pascal_triangle(1), [[1]])

    def test_2_row(self):
        self.assertEqual(
        	pascal_triangle(2), 
        	[[1], [1, 1]]
        )

    def test_3_row(self):
        self.assertEqual(
        	pascal_triangle(3), 
        	[[1], [1, 1], [1, 2, 1]]
        )

    def test_4_row(self):
        self.assertEqual(
        	pascal_triangle(4), 
        	[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
        )

    def test_5_row(self):
        self.assertEqual(
        	pascal_triangle(5), 
        	[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        )


if __name__ == "__main__":
    unittest.main()

