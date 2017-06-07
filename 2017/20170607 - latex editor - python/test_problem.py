#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_uma_raiz(self):
        self.assertEqual(
'''
A''', latex('\pstree{\Tcircle{A}}{}'))


    def test_uma_raiz_e_um_no(self):
        self.assertEqual(
'''
 A
B''', latex('\pstree{\Tcircle{A}}{\Tcircle{B}}'))

    def test_uma_raiz_e_dois_nos(self):
        self.assertEqual(
'''
 A
B C''', latex('\pstree{\Tcircle{A}}{\Tcircle{B}\Tcircle{C}}'))
if __name__ == "__main__":
    unittest.main()

