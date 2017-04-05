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

    def test_D(self):
        self.assertEqual(3, teclado("D"))

    def test_AA(self):
        self.assertEqual(22, teclado("AA"))

    def test_AB(self):
        self.assertEqual(222, teclado("AB"))

    def test_E(self):
        self.assertEqual(33, teclado("E")) 

if __name__ == "__main__":
    unittest.main()

