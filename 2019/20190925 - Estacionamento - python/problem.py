#!/usr/bin/env python
# -*- coding: utf-8 -*-

def valor_total(tamanho, eventos):
    total = 0

    for evento in eventos:
        if evento[2] <= tamanho:
            total = total + 10
            tamanho = tamanho - evento[2]

    return total
