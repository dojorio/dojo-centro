#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_rodelas_com_zero(self):
        self.assertEqual(0,rodelas(0))

    def test_rodelas_com_1(self):
        self.assertEqual(1,rodelas(1))

    def test_rodelas_com_2(self):
        self.assertEqual(3,rodelas(2))

    def test_rodelas_com_3(self):
        self.assertEqual(7,rodelas(3))

    def test_rodelas_com_4(self):
        self.assertEqual(15,rodelas(4))

    def test_com_formula(self):
    	n = 60
    	self.assertEqual(2**n - 1, rodelas(n))

    def test_rodelas_com_203(self):
        self.assertEqual(15,rodelas(10))



if __name__ == "__main__":
    unittest.main()

