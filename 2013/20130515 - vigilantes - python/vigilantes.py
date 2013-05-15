#-*- coding: utf-8 -*-

def vigilantes(tabela, maximo):
    soma_abaixo_do_max = 0
    if sum(pontos for pontos, sabor in tabela) <= maximo:
        return sum(sabor for pontos, sabor in tabela)

    for (pontos, sabor) in tabela
        if pontos+soma_abaixo_do_max <= maximo:
            pontos+=soma_abaixo_do_max



    return max([sabor for (pontos, sabor) in tabela if pontos+soma_abaixo_do_max <= maximo]
        or [0])
