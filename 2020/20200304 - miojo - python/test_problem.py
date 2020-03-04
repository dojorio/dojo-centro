#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_1_1(self):
        self.assertEqual(miojo(1,1), 3)

    def test_1_2(self):
        self.assertEqual(miojo(2,5), 5)    


if __name__ == "__main__":
    unittest.main()

