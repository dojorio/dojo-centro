#-*- coding: utf-8 -*-

def vigilantes(tabela, maximo):

    if sum(pontos for pontos, sabor in tabela) <= maximo:
        return sum(sabor for pontos, sabor in tabela)

    return max([sabor for (pontos, sabor) in tabela if pontos <= maximo]
        or [0])
