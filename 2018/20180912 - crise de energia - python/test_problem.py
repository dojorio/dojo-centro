#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_n_3_m_1(self):
        # 1 = 1 - X
        # 2 = 1 - 3 - 2
        self.assertFalse(menor_salto(regioes=3, ultima_estacao=2, step=1))

    def test_n_3_m_2(self):
        # 1 = 1 - X
        # 2 = 1 - 3 - 2
        self.assertTrue(menor_salto(regioes=3, ultima_estacao=2, step=2))


if __name__ == "__main__":
    unittest.main()

