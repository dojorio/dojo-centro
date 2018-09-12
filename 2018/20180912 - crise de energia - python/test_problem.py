#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_n_3_u_2_m_2(self):
        self.assertEquals(menor_salto(regioes=3, ultima_estacao=2), 2)

    def test_n_3_u_3_m_2(self):
        self.assertEquals(menor_salto(regioes=3, ultima_estacao=3), 1)

    def test_n_4_u_2_m_5(self):
        self.assertEquals(menor_salto(regioes=4, ultima_estacao=2), 5)


if __name__ == "__main__":
    unittest.main()

