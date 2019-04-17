#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1288

class TestProblem(unittest.TestCase):
    def test_1(self):
        bombs  = ((100, 1),)
        cannon = 1
        castle = 100
        self.assertTrue(mission_accomplished(bombs, cannon, castle))

    def test_castle_2(self):
        bombs  = ((100, 1),)
        cannon = 1
        castle = 200
        self.assertFalse(mission_accomplished(bombs, cannon, castle))

    def test_castle_and_bomb_2(self):
        bombs  = ((200, 1),)
        cannon = 1
        castle = 200
        self.assertTrue(mission_accomplished(bombs, cannon, castle))

    def test_castle_300_and_bomb_200(self):
        bombs  = ((200, 1),)
        cannon = 1
        castle = 300
        self.assertFalse(mission_accomplished(bombs, cannon, castle))

    def test_castle_overweight(self):
        bombs  = ((300, 2),)
        cannon = 1
        castle = 300
        self.assertFalse(mission_accomplished(bombs, cannon, castle))

    def test_castle_300_bombs_200_100(self):
        bombs  = ((200, 1), (100, 1), )
        cannon = 2
        castle = 300
        self.assertTrue(mission_accomplished(bombs, cannon, castle))

if __name__ == "__main__":
    unittest.main()

