#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1470

import unittest
from problem import *


class TestRealProblem(unittest.TestCase):
    def test_1__0(self):
        fita_entrada = [1]
        fita_saida   = [1]
        self.assertEqual(dobra(fita_entrada, 0), fita_saida)

    def test_1__1(self):
        fita_entrada = [1]
        fita_saida   = [1]
        self.assertEqual(dobra(fita_entrada, 1), fita_saida)

    def test_1_2__0(self):
        fita_entrada = [1, 2]
        fita_saida   = [2, 1]
        self.assertEqual(dobra(fita_entrada, 0), fita_saida)


class TestProblem(unittest.TestCase):
    def test_1__1(self):
        fita_entrada = [1]
        fita_saida   = [1]
        self.assertTrue(dobra_ok(fita_entrada, fita_saida))

    def test_1__2(self):
        fita_entrada = [1]
        fita_saida   = [2]
        self.assertFalse(dobra_ok(fita_entrada, fita_saida))

    def test_2__1(self):
        fita_entrada = [2]
        fita_saida   = [1]
        self.assertFalse(dobra_ok(fita_entrada, fita_saida))    

    def test_1_1__1_1(self):
        fita_entrada = [1, 1]
        fita_saida   = [1, 1]
        self.assertTrue(dobra_ok(fita_entrada, fita_saida))    

    def test_1_2__2_1(self):
        fita_entrada = [1, 2]
        fita_saida   = [2, 1]
        self.assertTrue(dobra_ok(fita_entrada, fita_saida))    

    def test_1_1__2(self):
        fita_entrada = [1, 1]
        fita_saida   = [2]
        self.assertTrue(dobra_ok(fita_entrada, fita_saida))    

    def test_10_20__15(self):
        fita_entrada = [10, 20]
        fita_saida   = [15]
        self.assertFalse(dobra_ok(fita_entrada, fita_saida))    

    def test_1_2_3__1_5(self):
        fita_entrada = [1, 2, 3]
        fita_saida   = [1, 5]
        self.assertTrue(dobra_ok(fita_entrada, fita_saida))

    def test_1_2_3__1_3_2(self):
        fita_entrada = [1, 2, 3]
        fita_saida   = [1, 3, 2]
        self.assertFalse(dobra_ok(fita_entrada, fita_saida))

    def test_1_2_3__4_2(self):
        fita_entrada = [1, 2, 3]
        fita_saida   = [4, 2]
        self.assertFalse(dobra_ok(fita_entrada, fita_saida))

    def test_1_2_3__2_4(self):
        fita_entrada = [1, 2, 3]
        fita_saida   = [2, 4]
        self.assertFalse(dobra_ok(fita_entrada, fita_saida))

    def test_1_2_3__3_3(self):
        fita_entrada = [1, 2, 3]
        fita_saida   = [3, 3]
        self.assertTrue(dobra_ok(fita_entrada, fita_saida))

    def test_1_2_3__1_5(self):
        fita_entrada = [1, 2, 3]
        fita_saida   = [1, 5]
        self.assertTrue(dobra_ok(fita_entrada, fita_saida))

    def test_1_2_3__6(self):
        fita_entrada = [1, 2, 3]
        fita_saida   = [6]
        self.assertTrue(dobra_ok(fita_entrada, fita_saida))

    def test_1_2_3__1_2_12(self):
        fita_entrada = [1, 2, 3, 4, 5]
        fita_saida   = [1, 2, 12]
        self.assertTrue(dobra_ok(fita_entrada, fita_saida))

    # def test_1_2_3__2_1_12(self):
    #     fita_entrada = [1, 2, 3, 4, 5]
    #     fita_saida   = [2, 1, 12]
    #     self.assertFalse(dobra_ok(fita_entrada, fita_saida))

if __name__ == "__main__":
    unittest.main()

