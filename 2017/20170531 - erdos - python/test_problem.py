#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def teste_numero_de_erdos_eh_0(self):
        self.assertEqual({'Erdos': 0}, numero_de_erdos([['Erdos']]))

    def teste_coautor_1(self):
        self.assertEqual(
            {
                'Erdos': 0,
                'Carlos': 1
            }
            , numero_de_erdos([['Erdos'],['Erdos','Carlos']]))

    def teste_coautores_1(self):
        self.assertEqual(
            {
                'Erdos': 0,
                'Carlos': 1,
                'Juliana': 1,
            }
            , numero_de_erdos([['Erdos'],['Erdos','Carlos'],['Erdos', 'Juliana']]))

    def teste_coautores_2(self):
        self.assertEqual(
            {
                'Erdos': 0,
                'Carlos': 1,
                'Juliana': 1,
                'Ana': 2,
            }
            , numero_de_erdos([['Erdos'],['Erdos','Carlos'],
                               ['Erdos', 'Juliana'], ['Juliana', 'Ana']]))

    def teste_coautores_2_2(self):
        self.assertEqual(
            {
                'Erdos': 0,
                'Carlos': 1,
                'Juliana': 1,
                'Ana': 2,
                'Julia': 2,
            }
            , numero_de_erdos([['Erdos'],['Erdos','Carlos'],
                               ['Erdos', 'Juliana'], ['Juliana', 'Ana'],
                               ['Juliana', 'Julia']]))

    def teste_coautores_3(self):
        self.assertEqual(
            {
                'Erdos': 0,
                'Carlos': 1,
                'Juliana': 1,
                'Ana': 2,
                'Julia': 2,
                'Marcos': 2
            }
            , numero_de_erdos([['Erdos'],['Erdos','Carlos'],
                               ['Erdos', 'Juliana'], ['Juliana', 'Ana'],
                               ['Juliana', 'Julia'], ['Juliana', 'Julia', 'Marcos']
                               ]))

    def teste_coautores_3(self):
        self.assertEqual(
            {
                'Erdos': 0,
                'Carlos': 1,
                'Juliana': 1,
                'Ana': 2,
                'Julia': 2,
                'Marcos': 2
            }
            , numero_de_erdos([['Erdos'],['Erdos','Carlos'],
                               ['Erdos', 'Juliana'], ['Juliana', 'Ana'],
                               ['Juliana', 'Julia'], ['Juliana', 'Julia', 'Marcos']
                               ,['Julia','Murta',]
                               ]))

if __name__ == "__main__":
    unittest.main()

