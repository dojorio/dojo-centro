#!/usr/bin/env python
# -*- coding: utf-8 -*-

def dobra(fita_entrada, pos):
    first, second = fita_entrada[:pos], fita_entrada[pos:]
    if len(first) > len(second):
        for ind, number in enumerate(reversed(first)):
            
    if pos in (0, len(fita_entrada)):
        return fita_entrada[::-1]
    if pos == 1:
        return [sum(fita_entrada)]
    return fita_entrada

def dobra_ok(fita_entrada, fita_saida):
    if len(fita_saida) == len(fita_entrada) - 1 != 1:
        fita_entrada_dobrada_pelo_fim    = [fita_entrada[0], sum(fita_entrada[-2:])]
        fita_entrada_dobrada_pelo_comeco = [sum(fita_entrada[:2]), fita_entrada[-1]]

        return fita_saida in (fita_entrada_dobrada_pelo_comeco, 
            fita_entrada_dobrada_pelo_fim)

    if len(fita_entrada) == len(fita_saida):
        return fita_entrada in (fita_saida, fita_saida[::-1])
    
    return sum(fita_entrada) == sum(fita_saida)
