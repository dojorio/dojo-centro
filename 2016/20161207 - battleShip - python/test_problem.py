#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_a1(self):
        self.assertEqual([('a1',)],CriaMatriz([('a1',)],['a1']))

    def test_vazio(self):
    	self.assertEqual([],CriaMatriz([('a1',)],['f1']))

    def test_a1a2_a1(self):
    	self.assertEqual([],CriaMatriz([('a1','a2')],['a1']))
	
if __name__ == "__main__":
    unittest.main()

