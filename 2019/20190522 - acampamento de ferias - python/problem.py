#!/usr/bin/env python
# -*- coding: utf-8 -*-

def gira(criancas):
    pos = 0
    crianca, numero = list(criancas.items())[pos]
    # 2_1_1
    # 'Jose': 1,
    # 'Joao': 2
    while len(criancas) > 1:
        #crianca, numero = list(criancas.items())[pos]
        if not numero % 2:
            pos = pos + numero
            while pos > len(criancas):
                pos -= len(criancas)
        else:
            pos = pos - numero
            while pos < 0:
                pos += len(criancas)
        # crianca_a_ser_removida = crianca
        crianca, numero = list(criancas.items())[pos]
        criancas.pop(crianca)
        pos -= 1

        
    return list(criancas.keys())[0]     

    # if list(criancas.values())[0] % 2 == 0:
    #     return list(criancas)[1]
    # return list(criancas)[0]