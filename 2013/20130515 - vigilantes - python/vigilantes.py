#-*- coding: utf-8 -*-

def iterar(tabela, maximo, i):
    if i>=len(tabela):
        return 0

    pontos, sabor = tabela[i]
    if maximo - pontos >= 0:
        return sabor + iterar(tabela, maximo-pontos, i+1)
    else:
        return iterar(tabela, maximo, i+1)

def vigilantes(tabela, maximo):
    soma_pontos_abaixo_do_max = 0
    soma_sabor = 0

    ordenador = lambda (pontos, sabor): sabor

    tabela = sorted(tabela, key = ordenador)
    tabela_invertida = tabela[::-1]

    return max(
        iterar(tabela, maximo, 0),
        iterar(tabela_invertida, maximo, 0))
