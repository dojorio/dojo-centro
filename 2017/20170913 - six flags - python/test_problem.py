#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/en/problems/view/1487

import unittest
from problem import *

# 0 ≤ N ≤ 100 e 0 ≤ T ≤ 600,
        # 5 60
        # 10 30
        # 20 32
        # 5 4
        # 50 90
        # 22 45

class TestProblem(unittest.TestCase):
    def test_uma_atracao(self):
        tempo = 60
        atracoes = (
            (10, 30),
        )
        self.assertEqual(180, sixflags(tempo, atracoes))

    def test_outra_atracao_240(self):
        tempo = 60
        atracoes = (
            (10, 40),
        )
        self.assertEqual(240, sixflags(tempo, atracoes))

    def test_menos_tempo(self):
        tempo = 60
        atracoes = (
            (35, 40),
        )
        self.assertEqual(40, sixflags(tempo, atracoes))

    def test_sem_tempo_suficiente(self):
        tempo = 60
        atracoes = (
            (61, 40),
        )
        self.assertEqual(0, sixflags(tempo, atracoes))

    def test_sem_tempo_suficiente_de_novo_caramba(self):
        tempo = 50
        atracoes = (
            (51, 40),
        )
        self.assertEqual(0, sixflags(tempo, atracoes))

    def test_duas_atracoes(self):
        tempo = 60
        atracoes = (
            (25, 30), (10, 11),
        )
        self.assertEqual(71, sixflags(tempo, atracoes))




if __name__ == "__main__":
    unittest.main()
