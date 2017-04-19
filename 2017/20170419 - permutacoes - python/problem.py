#!/usr/bin/env python
# -*- coding: utf-8 -*-

def permutacoes(entrada):
    t = []
    if len (entrada) > 1:
        t[0] =  entrada
        t[1] = reversed(entrada)

    return tuple(t)