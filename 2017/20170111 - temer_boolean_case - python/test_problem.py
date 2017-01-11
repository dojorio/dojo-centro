#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *

class TestTemerUmCaracter(unittest.TestCase):
    def test_vai_ter_impeachment(self):
        self.assertTrue(impeachment("s"))

    def test_nao_vai_ter_golpe(self):
        self.assertFalse(impeachment("n"))

    def test_golpista_deu_golpe(self):
        self.assertTrue(impeachment("S"))

    def test_pessoa_nao_deu_golpe(self):
        self.assertFalse(impeachment("N"))

    def test_dois_golpistas_deu_golpe(self):
        self.assertTrue(impeachment("ss"))

    def test_um_a_favor_e_um_contra(self):
        self.assertFalse(impeachment("sn"))

    def test_influencia_golpista_deu_golpe(self):
        self.assertTrue(impeachment("Sn"))

    def test_influencia_nao_deu_golpe(self):
        self.assertFalse(impeachment("Ns"))

    def test_influente_golpista_irrelevante(self):
        self.assertFalse(impeachment("nS"))

    def test_influente_ok_irrelevante(self):
        self.assertFalse(impeachment("sN"))

    def test_tres_golpistas_deu_golpe(self):
        self.assertTrue(impeachment("sss"))

    def test_tres_nao_golpistas_nao_deu_golpe(self):
        self.assertFalse(impeachment("nnn"))

    def test_dois_nao_golpistas_um_golpista_nao_deu_golpe(self):
        self.assertFalse(impeachment("nns"))

    def test_ssn_deu_impeachment(self):
        self.assertTrue(impeachment("ssn"))

    def test_Nss_nao_vai_ter_golpe(self):
        self.assertFalse(impeachment("Nss"))

if __name__ == "__main__":
    unittest.main()

