#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_primeira_estrofe(self):
        balao = Balao()

        self.assertTrue(balao.cair())

if __name__ == "__main__":
    unittest.main()

