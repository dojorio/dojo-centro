#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://www.urionlinejudge.com.br/judge/en/problems/view/1128

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    '''
        number of intersections (2 ≤ N ≤ 2000)
        number of streets (2 ≤ M ≤ N(N−1)/2)
    '''
    def test_two_intersections_connected(self):
        # 1 -> 2
        # 2 -> 1
        streets = [
            (1, 2, 2),
        ]
        self.assertTrue(is_connected(streets))

    def test_two_intersections_not_connected(self):
        streets = [
            (1, 2, 1),
        ]
        self.assertFalse(is_connected(streets))

    def test_two_intersections_connected_02(self):
        streets = [
            (2, 1, 2),
        ]
        self.assertTrue(is_connected(streets))


if __name__ == "__main__":
    unittest.main()

