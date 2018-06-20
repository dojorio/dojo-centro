#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1520

import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def test_(self):
        finder = ScrewFinder([(1, 1)])
        self.assertEqual([], finder.find(2))


if __name__ == "__main__":
    unittest.main()
