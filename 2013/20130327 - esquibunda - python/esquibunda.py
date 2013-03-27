#-*- coding: utf-8 -*-

def rindex(lista, valor):
    return len(lista) - lista[-1::-1].index(valor) -1

def esquibunda(montanha):
    if not montanha:
        return 0

    pista = montanha[0]

    numero_de_elementos_unicos = len(set(pista))
    if numero_de_elementos_unicos != len(pista):
        return numero_de_elementos_unicos

    max_index = pista.index(max(pista))
    min_index = rindex(pista, min(pista))

    return abs(max_index - min_index) + 1
