#-*- coding: utf-8 -*-

def vigilantes(tabela, maximo):
    if len(tabela)==2:
        if tabela[1][1] > tabela[0][1] and tabela[1][0] <= maximo:
            return tabela[1][1]
    return tabela[0][1]
