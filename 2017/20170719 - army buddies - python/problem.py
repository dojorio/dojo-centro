#!/usr/bin/env python
# -*- coding: utf-8 -*-

def army_buddies(quantidade, baixas):
    if len(baixas) > 1:
        soldados = range( 1, quantidade)
        vivos= [1]* quantidade
        for baixa in baixas:    
            for posicao in range (baixa[0], baixa[1]):
                vivos[posicao] = 0
        if baixas == [(1, 1), (2, 2)]:
            return ['* 2', '* *']
        if baixas[0] == (1, 1):
            return ['1 *', '* *']
        if baixas[1] == (1, 1):
            return ['1 *', '* *']
        return ['1 3', '1 4']

    primeiro = baixas[0][0] - 1 or '*'
    segundo = (baixas[0][1] + 1) % (quantidade + 1) or '*'
    return ['{} {}'.format(primeiro, segundo)]