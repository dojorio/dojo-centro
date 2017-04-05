#!/usr/bin/env python
# -*- coding: utf-8 -*-

def rodelas(n):
    if n == 0:
        return 0

    resultado = 1

    for i in range(1, n):
        resultado = 2 * resultado + 1
    
    return resultado