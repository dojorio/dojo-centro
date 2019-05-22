#!/usr/bin/env python
# -*- coding: utf-8 -*-

def gira(criancas):
    pos = 0
    # 2_1_1
    while len(criancas) > 1:
        crianca, numero = list(criancas.items())[pos]
        if not numero % 2:
            pos = pos + numero
        else:
            pos = pos - numero
        
        return list(criancas.keys())[pos]     

    if list(criancas.values())[0] % 2 == 0:
        return list(criancas)[1]
    return list(criancas)[0]