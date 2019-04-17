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

    def test_castle_300_bombs_200_99(self):
        bombs  = ((200, 1), (99, 1), )
        cannon = 2
        castle = 300
        self.assertFalse(mission_accomplished(bombs, cannon, castle))

    def test_castle_300_bombs_200_100_overweight(self):
        bombs  = ((200, 1), (100, 1), )
        cannon = 1
        castle = 300
        self.assertFalse(mission_accomplished(bombs, cannon, castle))

    def test_castle_300_bombs_300_100_overweight(self):
        bombs  = ((300, 1), (100, 1), )
        cannon = 1
        castle = 300
        self.assertTrue(mission_accomplished(bombs, cannon, castle))

    def test_castle_300_bombs_100_300_overweight(self):
        bombs  = ((100, 1), (300, 1), )
        cannon = 1
        castle = 300
        self.assertTrue(mission_accomplished(bombs, cannon, castle))

    def test_castle_300_bombs_100_100_100(self):
        bombs = ((100, 1), (100, 1), (100, 1), )
        cannon = 3
        castle = 300
        self.assertTrue(mission_accomplished(bombs, cannon, castle))

    def test_castle_400_bombs_100_100_100(self):
        bombs = ((100, 1), (100, 1), (100, 1), )
        cannon = 3
        castle = 400
        self.assertFalse(mission_accomplished(bombs, cannon, castle))

    def test_castle_400_bombs_200_200_100_fake_overweight(self):
        bombs = ((200, 1), (200, 1), (100, 1), )
        cannon = 2
        castle = 400
        self.assertTrue(mission_accomplished(bombs, cannon, castle))

    def test_castle_400_bombs_200_100_200_fake_overweight(self):
        bombs = ((200, 1), (100, 1), (200, 1), )
        cannon = 2
        castle = 400
        self.assertTrue(mission_accomplished(bombs, cannon, castle))

    def test_castle_400_bombs_100_200_200_fake_overweight(self):
        bombs = ((100, 1), (200, 1), (200, 1), )
        cannon = 2
        castle = 400
        self.assertTrue(mission_accomplished(bombs, cannon, castle))

    def test_castle_400_bombs_100_200_200_overweight(self):
        bombs = ((200, 1), (200, 2), (200, 1), )
        cannon = 2
        castle = 400
        self.assertTrue(mission_accomplished(bombs, cannon, castle))

if __name__ == "__main__":
    unittest.main()

