#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_1_minuto(self):
        value = '1 1 1 2'
        expected = 'O JOGO DUROU 0 HORA(S) E 1 MINUTO(S)'
        self.assertEqual(expected, time(value))


if __name__ == "__main__":
    unittest.main()

