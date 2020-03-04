#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_1_1(self):
        self.assertEqual(miojo(1,1), 3)

    def test_2_5(self):
        self.assertEqual(miojo(2,5), 5)

    def test_2_7(self):
        self.assertEqual(miojo(2,7), 7)

    def test_2_9(self):
        self.assertEqual(miojo(2,9), 9)

    def test_2_4(self):
        self.assertEqual(miojo(2,4), 'ampulhetas inválidas')

    def test_2_6(self):
        self.assertEqual(miojo(2,6), 'ampulhetas inválidas')

    def test_6_4(self):
        self.assertEqual(miojo(6,4), 'ampulhetas inválidas')

    def test_5_2(self):
        self.assertEqual(miojo(5,2), 5)
    
    def test_2_11(self):
        self.assertEqual(miojo(2,11), 11)          
    
    def test_2_1(self):
        self.assertEqual(miojo(2,1), 3)

    def test_7_2(self):
        self.assertEqual(miojo(7,2), 7)

    def test_5_7(self):
        self.assertEqual(miojo(5,7), 10)        

    def test_5_8(self):
        self.assertEqual(miojo(5,8), 8)

    def test_6_9(self):
        self.assertEqual(miojo(6,9), 9)

if __name__ == "__main__":
    unittest.main()

