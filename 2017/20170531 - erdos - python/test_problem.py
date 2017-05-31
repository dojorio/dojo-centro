#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def teste_ele_mesmo(self):
        self.assertEqual({'Erdos':0}, numero_de_erdos([['Erdos']]))

    def teste_coautor_1(self):
        self.assertEqual(
            {
                'Erdos':0,
                'Carlos':1
            }
            , numero_de_erdos([['Erdos'],['Erdos','Carlos']]))

    def teste_coautores_1(self):
        self.assertEqual(
            {
                'Erdos':0,
                'Carlos':1,
                'Juliana':1,
            }
            , numero_de_erdos([['Erdos'],['Erdos','Carlos'],['Erdos', 'Juliana']]))

if __name__ == "__main__":
    unittest.main()

