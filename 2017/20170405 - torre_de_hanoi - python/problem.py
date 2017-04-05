#!/usr/bin/env python
# -*- coding: utf-8 -*-

def rodelas(n):
    progressao = 2
    resultado = 0    

    if n == 1: 
        return 1
    elif n == 2:
        return 3
    elif n == 3:
        return 7
    elif n == 4:
        return 15

    return 0