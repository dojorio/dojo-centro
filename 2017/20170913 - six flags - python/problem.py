#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sixflags(tempo, atracoes):
    satisfacao = 0
    while tempo >= atracoes[0][0]:
        tempo -= atracoes[0][0]
        satisfacao += atracoes[0][1]
    return satisfacao
