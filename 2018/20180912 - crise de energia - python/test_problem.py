#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_n_3_u_2_m_1(self):
        # 1 = 1 - X
        # 2 = 1 - 3 - 2
        self.assertFalse(menor_salto(regioes=3, ultima_estacao=2, step=1))

    def test_n_3_u_2_m_2(self):
        # 1 = 1 - X
        # 2 = 1 - 3 - 2
        self.assertTrue(menor_salto(regioes=3, ultima_estacao=2, step=2))

    def test_n_3_u_3_m_2(self):
        # 1 = 1 - 2 - 3
        self.assertTrue(menor_salto(regioes=3, ultima_estacao=3, step=1))

    def test_n_4_u_3_m_1(self):
        # 1 = 1 - 2 - X
        self.assertFalse(menor_salto(regioes=4, ultima_estacao=3, step=1))



if __name__ == "__main__":
    unittest.main()

