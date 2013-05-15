#-*- coding: utf-8 -*-

def vigilantes(tabela, maximo):
    soma_pontos_abaixo_do_max = 0
    soma_sabor = 0

    ordenador = lambda (pontos, sabor): -sabor/float(pontos)

    for pontos, sabor in sorted(tabela, key = ordenador):
        if pontos + soma_pontos_abaixo_do_max <= maximo:
            soma_pontos_abaixo_do_max+=pontos
            soma_sabor+=sabor

    return soma_sabor
