#!/usr/bin/env python
# -*- coding: utf-8 -*-

def gira(criancas):
    pos = 0
    # 2_1_1
    while len(criancas) > 1:
        crianca, numero = list(criancas.items())[pos]
        if not numero % 2:
            pos = pos + numero
            if pos > len(criancas):
                pos -= len(criancas)


        else:
            pos = pos - numero
            if pos < 0:
                pos += len(criancas)
        criancas.pop(crianca)
        
    return list(criancas.keys())[0]     

    # if list(criancas.values())[0] % 2 == 0:
    #     return list(criancas)[1]
    # return list(criancas)[0]