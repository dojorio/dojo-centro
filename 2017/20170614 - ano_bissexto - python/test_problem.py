#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestAnoBissexto(unittest.TestCase):
    def test_1600_eh_bissexto(self):
        self.assertTrue(ano_bissexto(1600))

    def test_1742_nao_eh_bissexto(self):
        self.assertFalse(ano_bissexto(1742))

    def test_1_nao_eh_bissexto(self):
        self.assertFalse(ano_bissexto(1))

    def test_4_eh_bissexto(self):
        self.assertTrue(ano_bissexto(4))
if __name__ == "__main__":
    unittest.main()

