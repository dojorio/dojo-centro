#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *

class TestBuracos(unittest.TestCase):

    def test_B_tem_2_buracos(self):
        self.assertEqual(quantidade_buracos('B'), 2)

    def test_0_buraco(self):
        letras_com_0 = 'CEFGHIJKLMNSTUVWXYZ '
        for letra in letras_com_0:
            self.assertEqual(quantidade_buracos(letra), 0, letra)

    def test_1_buraco(self):
        letras_com_1 = 'ADOPQRabdegopq'
        for letra in letras_com_1:
            self.assertEqual(quantidade_buracos(letra), 1, letra)

    def test_AA(self):
        self.assertEqual(quantidade_buracos('AA'), 2)

    def test_AAA(self):
        self.assertEqual(quantidade_buracos('AAA'), 3)

    def test_JEFFERSON(self):
        self.assertEqual(quantidade_buracos('JEFFERSON OLIVEIRA'), 5)
    



if __name__ == "__main__":
    unittest.main()

