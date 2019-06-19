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

    def test_tudo_errado(self):
        testemunha = Testemunha(2, 1, 1)
        self.assertEqual(testemunha.pergunta(2, 2, 2), 2)


if __name__ == "__main__":
    unittest.main()
