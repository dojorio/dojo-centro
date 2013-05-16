#-*- coding: utf-8 -*-

def iterar(tabela, maximo, i):
    if i>=len(tabela):
        return 0

    pontos, sabor = tabela[i]
    if (maximo - pontos < 0 ):
        return iterar (tabela, maximo, i+1)
    return max(sabor + iterar(tabela, maximo-pontos, i+1),
        iterar(tabela, maximo, i+1))

def vigilantes(tabela, maximo):

    return iterar(tabela, maximo, 0)
