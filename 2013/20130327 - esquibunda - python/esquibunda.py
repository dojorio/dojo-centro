#-*- coding: utf-8 -*-

def ateh_quando(lista, index, passo):
    tamanho = 1
    try:
        while lista[index] > lista[index+passo] and 0 <= index+passo < len(lista):
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

    def ateh_onde(index):
        return max (ateh_quando(pista, index, +1), ateh_quando(pista, index, -1))


    return max(map(ateh_onde, range(len(pista))))

