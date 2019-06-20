#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.dojopuzzles.com/problemas/exibe/descubra-o-assassino/

# Suspeitos:
# 1   Charles B. Abbage
# 2   Donald Duck Knuth
# 3   Ada L. Ovelace
# 4   Alan T. Uring
# 5   Ivar J. Acobson
# 6   Ras Mus Ler Dorf

# Armas:
# 1   Peixeira
# 2   DynaTAC 8000X (o primeiro aparelho celular do mundo)
# 3   Trezoitão
# 4   Trebuchet
# 5   Maça
# 6   Gládio

# Locais:
# 1   Redmond
# 2   Palo Alto
# 3   San Francisco
# 4   Tokio
# 5   Restaurante no Fim do Universo
# 6   São Paulo
# 7   Cupertino
# 8   Helsinki
# 9   Maida Vale
# 10  Toronto

import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def test_tudo_errado(self):
        testemunha = Testemunha(1, 1, 1)
        self.assertEqual(testemunha.pergunta(2, 2, 2), 1)

    def test_so_suspeito_certo(self):
        testemunha = Testemunha(2, 1, 1)
        self.assertEqual(testemunha.pergunta(2, 2, 2), 2)
    
    def test_so_local_errado(self):
        testemunha = Testemunha(2, 2, 1)
        self.assertEqual(testemunha.pergunta(2, 2, 2), 3)        

    def test_tudo_certo(self):
        testemunha = Testemunha(2, 2, 2)
        self.assertEqual(testemunha.pergunta(2, 2, 2), 0)

    def test_tentativas(self):
        testemunha = Testemunha(1, 1, 1)
        detetive = Detetive(testemunha)
        self.assertEqual(detetive.tentativas(10), [1,1,1])

    def test_uma_tentativa(self):
        testemunha = Testemunha(2, 1, 1)
        detetive = Detetive(testemunha)
        self.assertEqual(detetive.tentativas(1), 1)

    def test_duas_tentativas(self):
        testemunha = Testemunha(2, 1, 1)
        detetive = Detetive(testemunha)
        self.assertEqual(detetive.tentativas(2), [2, 1, 1])

    def test_tres_tentativas(self):
        testemunha = Testemunha(2, 2, 1)
        detetive = Detetive(testemunha)
        self.assertEqual(detetive.tentativas(3), [2, 2, 1])

    def test_duas_tentativas_suspeito_errado(self):
        testemunha = Testemunha(3, 1, 1)
        detetive = Detetive(testemunha)
        self.assertEqual(detetive.tentativas(2), 1)

    def test_duas_tentativas_local_errado(self):
        testemunha = Testemunha(1, 1, 2)
        detetive = Detetive(testemunha)
        self.assertEqual(detetive.tentativas(2), [1, 1, 2])

    def test_dez_tentativas_local_errado(self):
        testemunha = Testemunha(4, 4, 10)
        detetive = Detetive(testemunha)
        self.assertEqual(detetive.tentativas(10), 3)


    def test_dez_tentativas_arma_errado(self):
        testemunha = Testemunha(6, 6, 10)
        detetive = Detetive(testemunha)
        self.assertEqual(detetive.tentativas(10), 2)

if __name__ == "__main__":
    unittest.main()
