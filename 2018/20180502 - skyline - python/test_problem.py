#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://codechen.blogspot.com.br/2015/06/leetcode-skyline-problem.html

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    # [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ]
    # [ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]
    def test_one_building(self):
        coordinates = [
            [2, 9, 10]
        ]
        skyline_coordinates = [
            [2, 10], 
            [9, 0],
        ]
        self.assertEqual(skyline(coordinates), skyline_coordinates)


if __name__ == "__main__":
    unittest.main()

