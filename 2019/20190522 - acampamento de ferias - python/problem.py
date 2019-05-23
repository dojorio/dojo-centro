#!/usr/bin/env python
# -*- coding: utf-8 -*-

def gira(criancas):
    pos = 0
    crianca, numero = list(criancas.items())[pos]
    while len(criancas) > 1:
        if not numero % 2:
            pos = pos + numero
            while pos >= len(criancas):
                pos -= len(criancas)
        else:
            pos = pos - numero
            while pos < 0:
                pos += len(criancas)
        crianca, numero = list(criancas.items())[pos]
        criancas.pop(crianca)
        if not numero % 2:
            pos -= 1

    return list(criancas.keys())[0]
