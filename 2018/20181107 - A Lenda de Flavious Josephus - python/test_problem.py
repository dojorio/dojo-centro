#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_quando_entrada_e_3_a_saida_deve_ser_1(self):
        self.assertEqual(1, josephus(3, 1))


if __name__ == "__main__":
    unittest.main()

