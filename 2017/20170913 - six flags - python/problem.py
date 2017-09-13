#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sixflags(tempo, atracoes):
    satisfacao = 0
    for atracao in sorted(atracoes):
        while tempo >= atracao[0]:
            tempo -= atracao[0]
            satisfacao += atracao[1]

    satisfacao02 = 0
    for atracao in sorted(atracoes, reverse=True):
        while tempo >= atracao[0]:
            tempo -= atracao[0]
            satisfacao02 += atracao[1]

    return max(satisfacao, satisfacao02)
