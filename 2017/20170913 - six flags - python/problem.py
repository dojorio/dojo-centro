#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sixflags(tempo, atracoes):
    satisfacao = 0
    for atracao in sorted(atracoes, reverse=True):
        while tempo >= atracao[0]:
            tempo -= atracao[0]
            satisfacao += atracao[1]
    return satisfacao