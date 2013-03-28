#-*- coding: utf-8 -*-

def ateh_quando(lista, index):
    pode_esquerda = index-1>=0 and lista[index] > lista[index-1]
    pode_direita = index+1<len(lista) and lista[index] > lista[index+1]

    return 1 + max(ateh_quando(lista, index-1) if pode_esquerda else 0,
               ateh_quando(lista, index+1) if pode_direita else 0)

def esquibunda(montanha):
    if not montanha:
        return 0

    if len(montanha) == 2:
        return 6

    pista = montanha[0]

    def ateh_onde(index):
        return ateh_quando(pista, index)

    return max(map(ateh_onde, range(len(pista))))

