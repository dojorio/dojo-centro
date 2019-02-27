#!/usr/bin/env python
# -*- coding: utf-8 -*-

def quantidade_buracos(texto):
    return sum(map(quantidade_buracos_em_1_letra, texto))

def quantidade_buracos_em_1_letra(texto):
    um_buraco = 'ADOPQRabdegopq'

    if texto == 'B':
        return 2

    if texto in um_buraco:
        return 1

    return 0
