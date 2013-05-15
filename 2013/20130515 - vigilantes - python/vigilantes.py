#-*- coding: utf-8 -*-

def vigilantes(tabela, maximo):
    soma_pontos_abaixo_do_max = 0
    soma_sabor_abaixo_do_max = 0

    if sum(pontos for pontos, sabor in tabela) <= maximo:
        return sum(sabor for pontos, sabor in tabela)

    for pontos, sabor in sorted(tabela, key = lambda x: -x[1]):
        if pontos + soma_pontos_abaixo_do_max <= maximo:
            soma_pontos_abaixo_do_max+=pontos
            soma_sabor_abaixo_do_max+=sabor



    return soma_sabor_abaixo_do_max
