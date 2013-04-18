#-*- coding: utf-8 -*-

def aeroporto(patio):
    y, x = max((linha.find('*'), x) for x, linha in enumerate(patio))

    return ver(map(list, patio), x, y) - 1

def ver(patio, x, y):
    if (not (0 <= x < len(patio)) or
        not (0 <= y < len(patio[0])) or
        patio[x][y] == "#" or
        patio[x][y] == "$"):
        return 0

    patio[x][y] = '$'
    return (ver(patio, x+1, y) +
            ver(patio, x-1, y) +
            ver(patio, x, y+1) +
            ver(patio, x, y-1) +
            1)
