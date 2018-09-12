#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_n_13_m_1(self):
        regioes = 13
        m = 1
        self.assertTrue(menor_salto(regioes, m))

    def test_n_17_m_5(self):
        regioes = 17
        m = 5
        self.assertFalse(menor_salto(regioes, m))

if __name__ == "__main__":
    unittest.main()

