#-*- coding: utf-8 -*-

def vigilantes(tabela, maximo):
    if len(tabela)==2:
        if tabela[1][1] > tabela[0][1]:
            return tabela[1][1]
    return tabela[0][1]
