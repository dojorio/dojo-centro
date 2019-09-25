#!/usr/bin/env python
# -*- coding: utf-8 -*-

def valor_total(tamanho, eventos):
    total = 0
    tamanhoUltimoCarro = 0

    for evento in eventos:
        if evento[0] == 'C':
            if evento[2] <= tamanho:
                tamanhoUltimoCarro = evento[2]
                total = total + 10
                tamanho = tamanho - evento[2]
        if evento[0] == 'S':
            tamanho = tamanho + tamanhoUltimoCarro


    return total
