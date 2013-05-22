#-*- coding: utf-8 -*-

def iterar(tabela, maximo, i):
    if i>=len(tabela) and maximo>=0: return 0
    if maximo < 0: return float('-inf')

    pontos, sabor = tabela[i]
    return max(
        iterar(tabela, maximo-pontos, i+1) + sabor,
        iterar(tabela, maximo, i+1))

def vigilantes(tabela, maximo):
    return iterar(tabela, maximo, 0)
