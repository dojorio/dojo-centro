#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.dojopuzzles.com/problemas/exibe/troco/

import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def test_1(self):
        self.assertEqual(change_for(3, 5), { 2: 1 })
    
    def test_2(self):
        self.assertEqual(change_for(20, 50), { 20: 1, 10: 1})

    def test_3(self):
        self.assertEqual(change_for(5, 10), { 5: 1 })

    def test_4(self):
        self.assertEqual(change_for(15, 20), { 5: 1 })

    def test_5(self):
        self.assertEqual(change_for(15, 15), { })


if __name__ == "__main__":
    unittest.main()
