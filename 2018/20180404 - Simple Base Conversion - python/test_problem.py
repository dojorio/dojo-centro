#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/en/problems/view/1199

import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def test_1_0x1(self):
        self.assertEqual('0x1', converter('1'))

    def test_2_0x2(self):
        self.assertEqual('0x2', converter('2'))

    def test_10_0xA(self):
        self.assertEqual('0xA', converter('10'))

    def test_11_0xB(self):
        self.assertEqual('0xB', converter('11'))

    def test_12_0xC(self):
        self.assertEqual('0xC', converter('12'))

if __name__ == "__main__":
    unittest.main()

