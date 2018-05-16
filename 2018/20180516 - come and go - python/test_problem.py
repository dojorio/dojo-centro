#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://www.urionlinejudge.com.br/judge/en/problems/view/1128

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    '''
        number of intersections (2 ≤ N ≤ 2000)
        (2 ≤ M ≤ N(N−1)/2)
    '''
    def test_two_intersections_connected(self):
        # 1 -> 2
        # 2 -> 1
        intersections = [
            (1, 2, 1),
            (2, 1, 1),
        ]
        self.assertEqual(is_connected(intersections), True)

    def test_three_intersections_not_connected(self):
        intersections = [
            (1, 2, 1),
            (2, 1, 1),
            (1, 3, 1),
        ]
        self.assertEqual(is_connected(intersections), True)


if __name__ == "__main__":
    unittest.main()

