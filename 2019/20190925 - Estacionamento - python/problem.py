#!/usr/bin/env python
# -*- coding: utf-8 -*-

def valor_total(tamanho, eventos):
    total = 0
    vagas = [None] * tamanho

    for evento in eventos:
        tipo  = evento[0]
        placa = evento[1]

        if tipo == 'C':
            inicioVaga = None
            tamanhoVaga = 0 
            tamanhoCarro = evento[2]

            for posicao in range(tamanho):
                if vagas[posicao] == None:
                    tamanhoVaga = tamanhoVaga + 1
                else:
                    tamanhoVaga = 0
                if tamanhoVaga == tamanhoCarro:
                    inicioVaga = posicao - tamanhoCarro + 1
                    break

            if inicioVaga != None:
                total = total + 10
                for metro in range(tamanhoCarro):
                    vagas[inicioVaga + metro] = placa

        if tipo == 'S':
            for vaga in range(tamanho):
                if vagas[vaga] == placa:
                    vagas[vaga] = None

    return total
