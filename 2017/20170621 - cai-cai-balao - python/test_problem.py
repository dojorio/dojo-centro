#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_primeira_queda(self):
        balao = Balao()
        self.assertTrue(balao.cair())
    
    def test_cair_2x(self):
        balao = Balao()
        balao.cair()
        balao.cair()
        self.assertTrue(balao.esta_ok())
    
    def test_cair_3x(self):
        balao = Balao()
        balao.cair()
        balao.cair()
        balao.cair()
        self.assertFalse(balao.esta_ok())

    def test_destino_da_queda(self):
        balao = Balao()
        balao.cair()
        balao.cair()
        balao.na('mão')
        self.assertTrue(balao.esta_ok())

    def test_destino_da_quedaInvalido(self):
        balao = Balao()
        balao.cair()
        balao.cair()
        balao.na('ali')
        self.assertFalse(balao.esta_ok())

if __name__ == "__main__":
    unittest.main()

