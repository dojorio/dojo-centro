#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestAnoBissexto(unittest.TestCase):
    def test_1600_eh_bissexto(self):
        self.assertTrue(ano_bissexto(1600))

    def test_2400_eh_bissexto(self):
        self.assertTrue(ano_bissexto(2400))

    def test_1742_nao_eh_bissexto(self):
        self.assertFalse(ano_bissexto(1742))

    def test_1_nao_eh_bissexto(self):
        self.assertFalse(ano_bissexto(1))

    def test_4_eh_bissexto(self):
        self.assertTrue(ano_bissexto(4))

    def test_8_eh_bissexto(self):
        self.assertTrue(ano_bissexto(8))

    def test_12_eh_bissexto(self):
        self.assertTrue(ano_bissexto(12))

    def test_16_eh_bissexto(self):
        self.assertTrue(ano_bissexto(16))

    def test_17_nao_eh_bissexto(self):
        self.assertFalse(ano_bissexto(17))

    def test_100_nao_eh_bissexto(self):
        self.assertFalse(ano_bissexto(100))

    def test_200_nao_eh_bissexto(self):
        self.assertFalse(ano_bissexto(200))

    def test_300_nao_eh_bissexto(self):
        self.assertFalse(ano_bissexto(300))

    def test_500_nao_eh_bissexto(self):
        self.assertFalse(ano_bissexto(500))

if __name__ == "__main__":
    unittest.main()

