#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def teste_ele_mesmo(self):
        self.assertEqual(0, numero_de_erdos(['Erdos']))

    def teste_coautor_1(self):
        self.assertEqual(1, numero_de_erdos(['Erdos', 'Daniel']))

if __name__ == "__main__":
    unittest.main()

