#!/usr/bin/env python
# -*- coding: utf-8 -*-

def menor_salto(regioes, ultima_estacao, step):
    if step == 2 or step == 1 and regioes == ultima_estacao:
        return True
    return False