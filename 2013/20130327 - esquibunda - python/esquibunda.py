#-*- coding: utf-8 -*-

def ateh_onde(lista, index, passo):
    tamanho = 1
    try:
        while lista[index] > lista[index+passo]:
            index += passo
            tamanho += 1
    except IndexError:
        pass

    return tamanho

def rindex(lista, valor):
    return len(lista) - lista[::-1].index(valor) -1

def esquibunda(montanha):
    if not montanha:
        return 0

    pista = montanha[0]

    max_index = pista.index(max(pista))

    return max(ateh_onde(pista, max_index, +1),
               ateh_onde(pista, max_index, -1))
