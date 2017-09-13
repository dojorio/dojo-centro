#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sixflags(tempo, atracoes):
    satisfacao = 0
    tempo1 = tempo
    for atracao in sorted(atracoes):
        while tempo1 >= atracao[0]:
            tempo1 -= atracao[0]
            satisfacao += atracao[1]

    satisfacao2 = 0
    for atracao in sorted(atracoes, reverse=True):
        while tempo >= atracao[0]:
            tempo -= atracao[0]
            satisfacao2 += atracao[1]

    return max(satisfacao, satisfacao2)
