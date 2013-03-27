#-*- coding: utf-8 -*-

def esquibunda(montanha):
    if not montanha:
        return 0



    pista = montanha[0]

    numero_de_elementos_unicos = len(set(pista))
    if numero_de_elementos_unicos != len(pista):
        return numero_de_elementos_unicos

    max_index = pista.index(max(pista))
    min_index = pista.index(min(pista))
    return abs(max_index - min_index) + 1
