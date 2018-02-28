#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.dojopuzzles.com/problemas/exibe/troco/

import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def test_1(self):
        self.assertEqual(change_for(3, 5), { 2: 1 })

    def test_3(self):
        self.assertEqual(change_for(5, 10), { 5: 1 })

if __name__ == "__main__":
    unittest.main()
