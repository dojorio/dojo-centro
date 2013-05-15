#-*- coding: utf-8 -*-

def vigilantes(tabela, maximo):
    soma_pontos_abaixo_do_max = 0
    soma_sabor = 0

    for pontos, sabor in sorted(tabela, key = lambda x: -x[1]):
        if pontos + soma_pontos_abaixo_do_max <= maximo:
            soma_pontos_abaixo_do_max+=pontos
            soma_sabor+=sabor

    return soma_sabor
