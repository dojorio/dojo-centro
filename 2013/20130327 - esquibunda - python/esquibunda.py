#-*- coding: utf-8 -*-

def esquibunda(montanha):
    if not montanha:
        return 0

    pista = montanha[0]

    if len(set(pista)) == 1:
        return 1

    if len(pista) == 3 and pista[1] == 1:
        return 2

    max_index = pista.index(max(pista))
    return max(max_index + 1, len(pista) - max_index)
