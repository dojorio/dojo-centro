#-*- coding: utf-8 -*-

def aeroporto(patio):
    espacos = 0

    for x, linha in enumerate(patio):
        y = linha.find('*')
        if y >= 0:
            entrada = (x, y)

    return ver(set(), patio, *entrada) - 1

def ver(vi, patio, x, y):
    if not (0 <= x < len(patio)):
        return 0

    if not (0 <= y < len(patio[0])):
        return 0

    if patio[x][y] == "#":
        return 0

    if (x,y) in vi:
        return 0

    vi.add((x,y))

    visitas = []
    visitas.append(ver(vi, patio, x+1, y))
    visitas.append(ver(vi, patio, x-1, y))
    visitas.append(ver(vi, patio, x, y+1))
    visitas.append(ver(vi, patio, x, y-1))

    return 1 + sum(visitas)
