#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_n_13_m_1(self):
        regioes = 13
        self.assertEqual(menor_salto(regioes), 1)

    def test_n_14_m_1(self):
        regioes = 14
        self.assertEqual(menor_salto(regioes), 2)


if __name__ == "__main__":
    unittest.main()

