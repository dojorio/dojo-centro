#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import permutations


def maior_na_ordem(tempo, atracoes):
    satisfacao = 0
    for atracao in atracoes:
        while tempo >= atracao[0]:
            tempo -= atracao[0]
            satisfacao += atracao[1]
    return satisfacao

def sixflags(tempo, atracoes):


    satisfacao1 = maior_na_ordem(tempo, sorted(atracoes))

    satisfacao2 = maior_na_ordem(tempo,
        sorted(atracoes, reverse=True))

    return max(satisfacao1, satisfacao2)
