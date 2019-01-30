#!/usr/bin/env python
# -*- coding: utf-8 -*-

def quantidade_buracos(texto):
    zero_buraco = "CEFGHIJKLMNSTUVWXYZ"

    if texto == 'B':
        return 2
    if texto in zero_buraco:
        return 0

    if len(texto) > 1:
        total = 0

        for letra in texto:
            total += quantidade_buracos(letra)

        return total

    return 1