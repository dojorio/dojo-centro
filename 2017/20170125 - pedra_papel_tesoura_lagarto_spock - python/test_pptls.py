#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from pptls import quem_ganha


class TestPPTLS(unittest.TestCase):
    def test_tesoura_corta_papel(self):
        self.assertEqual("tesoura corta papel", quem_ganha("tesoura", "papel"))

    def test_tesoura_lagarto(self):
    	self.assertEqual("tesoura decapita lagarto", quem_ganha("tesoura", "lagarto"))

    def test_papel_embrulha_pedra(self):
    	self.assertEqual("papel cobre pedra", quem_ganha("pedra", "papel"))

    def test_papel_refuta_spock(self):
    	self.assertEqual("papel refuta spock", quem_ganha("spock", "papel"))

    def test_tesoura_corta_papel_invertido(self):
    	self.assertEqual("tesoura corta papel", quem_ganha("papel", "tesoura"))

    def test_pedra_esmaga_lagarto(self):
    	self.assertEqual("pedra esmaga lagarto", quem_ganha("pedra", "lagarto"))

    def test_pedra_quebra_tesoura(self):
    	self.assertEqual("pedra quebra tesoura", quem_ganha("pedra", "tesoura"))

    def test_lagarto_envenena_spock(self):
    	self.assertEqual("lagarto envenena spock", quem_ganha("spock", "lagarto"))

    def test_lagarto_come_papel(self):
    	self.assertEqual("lagarto come papel", quem_ganha("lagarto", "papel"))

    def test_spock_vaporiza_pedra(self):
    	self.assertEqual("spock vaporiza pedra", quem_ganha("pedra", "spock"))

    def test_pedra_com_pedra(self):
    	self.assertEqual("Empate", quem_ganha("pedra", "pedra"))

if __name__ == "__main__":
    unittest.main()


