#!/usr/bin/env python
# -*- coding: utf-8 -*-

def quantidade_buracos(texto):

    total = 0

    for letra in texto:
        total += quantidade_buracos_em_1_letra(letra)

    return total

def quantidade_buracos_em_1_letra(texto):
    zero_buraco = "CEFGHIJKLMNSTUVWXYZ "

    if texto == 'B':
        return 2
    if texto in zero_buraco:
        return 0

    return 1
