#!/usr/bin/env python
# -*- coding: utf-8 -*-

def gira(criancas):
    pos = 0
    crianca, numero = list(criancas.items())[pos]
    # 'Joao': 1,
    # 'Jose': 1,
    # 'Maria': 1, 
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
        #pos -= 1

        
    return list(criancas.keys())[0]     

    # if list(criancas.values())[0] % 2 == 0:
    #     return list(criancas)[1]
    # return list(criancas)[0]