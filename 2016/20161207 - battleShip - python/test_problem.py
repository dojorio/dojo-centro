#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_CriaMatriz(self):
        self.assertEqual([('a1',)],CriaMatriz([('a1',)],[('a1',)]))


if __name__ == "__main__":
    unittest.main()

