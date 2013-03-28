#-*- coding: utf-8 -*-

def ateh_quando(lista, index, passo):
    tamanho = 1
    try:
        while lista[index] > lista[index+passo]:
            index += passo
            tamanho += 1
    except IndexError:
        pass

    return tamanho

def esquibunda(montanha):
    if not montanha:
        return 0

    pista = montanha[0]

    max_index = pista.index(max(pista))

    return max(map(lambda x: (ateh_quando(pista, x, +1)), range(len(pista))))
