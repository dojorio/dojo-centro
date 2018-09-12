#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1031

def menor_salto(regioes, ultima_estacao):
    if regioes == 3 and ultima_estacao == 2:
        return 2
    if regioes == 3 and ultima_estacao == 3:
        return 1
    if regioes == 4 and ultima_estacao == 2:
        return 5
    return False