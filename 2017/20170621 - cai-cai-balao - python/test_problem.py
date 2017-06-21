#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_primeira_queda(self):
        balao = Balao()
        self.assertTrue(balao.cai_cai())
    
    def test_cai_cai_2x(self):
        balao = Balao()
        balao.cai_cai()
        balao.cai_cai()
        self.assertTrue(balao.esta_ok())
    
    def test_cai_cai_3x(self):
        balao = Balao()
        balao.cai_cai()
        balao.cai_cai()
        balao.cai_cai()
        self.assertFalse(balao.esta_ok())

    def test_destino_da_queda(self):
        balao = Balao()
        balao.cai_cai()
        balao.cai_cai()
        balao.na('mão')
        self.assertTrue(balao.esta_ok())

    def test_destino_da_queda_invalido(self):
        balao = Balao()
        balao.cai_cai()
        balao.cai_cai()
        balao.na('ali')
        self.assertFalse(balao.esta_ok())

    def test_nao_cai_nao(self):
        balao = Balao()
        balao.cai_cai()
        balao.cai_cai()
        balao.na('mão')
        balao.nao_cai_nao()
        self.assertTrue(balao.esta_ok())

    def test_nao_cai_nao_________(self):
        balao = Balao()
        balao.cai_cai()
        balao.cai_cai()
        balao.na('mão')
        balao.nao_cai_nao()
        balao.nao_cai_nao()
        balao.nao_cai_nao()
        balao.nao_cai_nao()
        self.assertFalse(balao.esta_ok())

if __name__ == "__main__":
    unittest.main()

