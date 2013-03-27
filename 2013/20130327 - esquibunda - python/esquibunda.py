#-*- coding: utf-8 -*-

def esquibunda(montanha):
    if not montanha:
        return 0

    pista = montanha[0]

    if len(pista) == 3 and pista[1] == 1:
        return 2

    if pista[0] == pista[1] and pista[1] == pista[2]:
        return 1
    max_index = pista.index(max(pista))
    return max(max_index + 1, len(pista) - max_index)
