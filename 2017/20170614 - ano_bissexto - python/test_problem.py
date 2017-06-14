#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestAnoBissexto(unittest.TestCase):
    def test_retorno_eh_booleano(self):
        self.assertTrue(ano_bissexto(2000))

    def test_ano_eh_bissexto(self):
        self.assertFalse(ano_bissexto(2001))

if __name__ == "__main__":
    unittest.main()

