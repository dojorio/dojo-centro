#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *

class TestBuracos(unittest.TestCase):
    def test_A_tem_1_buraco(self):
        self.assertEqual(quantidade_buracos('A'), 1)

    def test_B_tem_2_buracos(self):
    	self.assertEqual(quantidade_buracos('B'), 2)

    def test_C_tem_0_buraco(self):
    	self.assertEqual(quantidade_buracos('C'), 0)

    def test_E_tem_0_buraco(self):
    	self.assertEqual(quantidade_buracos('E'), 0)

    def test_F_tem_0_buraco(self):
    	self.assertEqual(quantidade_buracos('F'), 0)

    def test_G_tem_0_buraco(self):
    	self.assertEqual(quantidade_buracos('G'), 0)

if __name__ == "__main__":
    unittest.main()

