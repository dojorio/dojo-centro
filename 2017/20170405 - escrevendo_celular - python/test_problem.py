#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_A(self):
        self.assertEqual(2, teclado("A"))
        
    def test_B(self):
        self.assertEqual(22, teclado("B"))

    def test_C(self):
        self.assertEqual(222, teclado("C"))

if __name__ == "__main__":
    unittest.main()

