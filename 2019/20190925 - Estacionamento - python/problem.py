#!/usr/bin/env python
# -*- coding: utf-8 -*-

def valor_total(tamanho, eventos):
    total = 0
    carros = {}

    for evento in eventos:
        tipo  = evento[0]
        placa = evento[1]

        if tipo == 'C':
            tamanhoCarro = evento[2]

            if tamanhoCarro <= tamanho:
                carros[placa] = tamanhoCarro
                total = total + 10
                tamanho = tamanho - tamanhoCarro

        if tipo == 'S':
            tamanhoCarroSaindo = carros[placa]
            tamanho = tamanho + tamanhoCarroSaindo


    return total
