#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1288

class TestProblem(unittest.TestCase):
    def test_1(self):
        bombs  = ((1, 1),)
        cannon = 1
        castle = 1
        self.assertTrue(mission_accomplished(bombs, cannon, castle))

    def test_2(self):
        bombs  = ((1, 1),)
        cannon = 1
        castle = 2
        self.assertFalse(mission_accomplished(bombs, cannon, castle))

if __name__ == "__main__":
    unittest.main()

