#!/usr/bin/env python
# -*- coding: utf-8 -*-

def rodelas(n):
    resultado =1
    progressao = 2
    if n >0 :
        for i in range (1,n):
            resultado = 2*resultado + 1

    return resultado