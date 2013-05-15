#-*- coding: utf-8 -*-

def vigilantes(tabela, maximo):
    return max([sabor for pontos, sabor in tabela if pontos <= maximo] or [0])

