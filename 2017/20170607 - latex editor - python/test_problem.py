#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_uma_raiz(self):
        self.assertEqual('A',
        	latex('\pstree{\Tcircle{A}}{}'))


    def test_uma_raiz_e_um_no(self):
        self.assertEqual(' A\n'
        	             'B',
        	latex('\pstree{\Tcircle{A}}{\Tcircle{B}}'))

    def test_uma_raiz_e_dois_nos(self):
        self.assertEqual(' A\n'
        				 'B C',
        	latex('\pstree{\Tcircle{A}}{\Tcircle{B}\Tcircle{C}}'))

    def test_arvore_nao_balanceada(self):
        self.assertEqual('  A\n'
						 ' B\n'
						 'C',
			latex('\pstree{\Tcircle{A}}{\pstree{\Tcircle{B}{Tcircle{C}}}'))

class TestProblemDic(unittest.TestCase):
    def test_uma_raiz(self):
        self.assertEqual({"A":[]},
        	MkDic('\pstree{\Tcircle{A}}{}'))



if __name__ == "__main__":
    unittest.main()

