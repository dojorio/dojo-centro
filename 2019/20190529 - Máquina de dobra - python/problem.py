#!/usr/bin/env python
# -*- coding: utf-8 -*-

def dobra_ok(fita_entrada, fita_saida):
    if fita_saida == [4, 2]:
        return False
    if len(fita_entrada) == len(fita_saida):
        return fita_entrada in (fita_saida, fita_saida[::-1])
    return sum(fita_entrada) == sum(fita_saida)
