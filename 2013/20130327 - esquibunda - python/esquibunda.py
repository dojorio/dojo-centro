#-*- coding: utf-8 -*-

def ateh_quando(lista, index):
    return 1 + max(ateh_quando(lista, index-1) if index-1>=0 and lista[index] > lista[index-1] else 0,
               ateh_quando(lista, index+1) if index+1<len(lista) and lista[index] > lista[index+1] else 0)

def esquibunda(montanha):
    if not montanha:
        return 0

    pista = montanha[0]

    max_index = pista.index(max(pista))

    def ateh_onde(index):
        return ateh_quando(pista, index)

    return max(map(ateh_onde, range(len(pista))))

