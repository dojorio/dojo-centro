#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def test_(self):
        self.assertEqual(0, numero_de_erdos(['Erdos']))

    def test_2(self):
        self.assertEqual(0, numero_de_erdos(['Erdos', 'Daniel']))

if __name__ == "__main__":
    unittest.main()

