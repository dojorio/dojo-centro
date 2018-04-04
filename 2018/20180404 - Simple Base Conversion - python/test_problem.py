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

    def test_13_0xD(self):
        self.assertEqual('0xD', converter('13'))

    def test_14_0xE(self):
        self.assertEqual('0xE', converter('14'))

    def test_15_0xF(self):
        self.assertEqual('0xF', converter('15'))

    def test_16_0x10(self):
        self.assertEqual('0x10', converter('16'))

    def test_17_0x11(self):
        self.assertEqual('0x11', converter('17'))

    def test_26_0x1A(self):
        self.assertEqual('0x1A', converter('26'))

    def test_32_0x20(self):
        self.assertEqual('0x20', converter('32'))
if __name__ == "__main__":
    unittest.main()

