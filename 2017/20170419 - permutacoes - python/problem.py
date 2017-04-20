#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import random

def permutacoes(entrada):
    
    saida = entrada 
    if len (entrada) == 2:
        return [entrada, entrada[::-1]]
    elif len(entrada) == 3:
        saida = []
        for d in entrada:
            saida.append(reversed(entrada[1:]))

    return [entrada] 