#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_quando_entrada_e_3_a_saida_deve_ser_3(self):
        self.assertEqual(3, josephus(4, 1))

    def test_quando_entrada_e_5_1_a_saida_deve_ser_5(self):
        self.assertEqual(5, josephus(5, 1))

    def test_quando_entrada_e_15_1_a_saida_deve_ser_15(self):
        self.assertEqual(15, josephus(15, 1))

    def test_quando_entrada_e_5_2_a_saida_deve_ser_3(self):
        self.assertEqual(3, josephus(5, 2))

    def test_quando_entrada_e_6_2_a_saida_deve_ser_5(self):
        self.assertEqual(5, josephus(6, 2))

    def test_quando_entrada_e_1234_233_a_saida_deve_ser_25(self):
        self.assertEqual(25, josephus(1234, 233))


if __name__ == "__main__":
    unittest.main()

