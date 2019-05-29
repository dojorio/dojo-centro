#!/usr/bin/env python
# -*- coding: utf-8 -*-

def dobra_ok(fita_entrada, fita_saida):
    if len(fita_entrada) > len(fita_saida) and fita_saida[0] == sum(fita_entrada):
        return True
    return fita_saida in [fita_entrada, fita_entrada[::-1]] 
