#-*- coding: utf-8 -*-

def aeroporto(patio):
    espacos = 0

    for x, linha in enumerate(patio):
        y = linha.find('*')
        if y >= 0:
            entrada = (x, y)

    return ver(set(), patio, *entrada) - 1

def ver(vi, patio, x, y):
    viu = not (0 <= x < len(patio))
    viu = viu or not (0 <= y < len(patio[0]))
    viu = viu or patio[x][y] == "#"
    viu = viu or (x,y) in vi
    if viu:
        return 0

    vi.add((x,y))

    return (ver(vi, patio, x+1, y) +
            ver(vi, patio, x-1, y) +
            ver(vi, patio, x, y+1) +
            ver(vi, patio, x, y-1)) + 1
