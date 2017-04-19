#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import random

def permutacoes(entrada):
    if len (entrada) == 2:
        return sorted([entrada, entrada[::-1]])
    elif len(entrada) == 3:
        saida = []
        lista = list(entrada)
        while len(saida) != math.factorial(len(entrada)):
            random.shuffle(lista)
            print (lista)
            if lista not in saida:
                saida.append(lista)
        return saida


    return [entrada]