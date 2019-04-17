#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *

class TestProblem(unittest.TestCase):

	matriz=[[8,8,3],[5,5,1],[3,4,2]]

	def retornar_quantidade_tabuleiros_L(matriz):
	    return matriz[0][0]

    def retornar_quantidade_lin_N(matriz):
	    return matriz[0][1]

    def retornar_quantidade_col_M(matriz):
	    return matriz[0][2]
    
    def test_dimensao_padrao(self):
        3 <= retornar_quantidade_tabuleiros_L(matriz) <= 100
        retornar_quantidade_lin_N(matriz) >= 8
        retornar_quantidade_col_M(matriz) <= 100

    def test_1(self):
        
        self.assertEqual(matriz, 2)




if __name__ == "__main__":
    unittest.main()

