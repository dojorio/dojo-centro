#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://www.urionlinejudge.com.br/judge/en/problems/view/1031

import unittest
from problem import *

class TestProblem(unittest.TestCase):
   
    def test_13(self):
        self.assertEqual(1, power_crisis(13))
   
    def test_14(self):
        self.assertEqual(18, power_crisis(14))
  
    def test_15(self):
        self.assertEqual(10, power_crisis(15))

    def test_16(self):
        self.assertEqual(11, power_crisis(16))

    def test_17(self):
        self.assertEqual(7, power_crisis(17))

    def test_18(self):
        self.assertEqual(29, power_crisis(18))

    def test_21(self):
        self.assertEqual(29, power_crisis(21))




if __name__ == "__main__":
    unittest.main()

