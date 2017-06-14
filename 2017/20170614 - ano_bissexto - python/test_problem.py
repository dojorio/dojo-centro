#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestAnoBissexto(unittest.TestCase):
    def test_retorno_eh_booleano(self):
        self.assertTrue(ano_bissexto(2000))


if __name__ == "__main__":
    unittest.main()

