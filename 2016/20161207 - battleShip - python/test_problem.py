#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_a1(self):
        self.assertEqual([('a1',)],CriaMatriz([('a1',)],['a1']))

    def test_vazio(self):
    	self.assertEqual([],CriaMatriz([('a1',)],['f1']))

   	def test_doisbarcos(self):
    	self.assertEqual([('b1',)],CriaMatriz([('a1',),('b1',)],['b1']))

    def test_a1c1_c1(self):
    	self.assertEqual([('c1',)],CriaMatriz([('a1',),('c1',)],['c1']))
	

if __name__ == "__main__":
    unittest.main()

