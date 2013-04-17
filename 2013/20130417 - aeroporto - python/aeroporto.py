#-*- coding: utf-8 -*-

def aeroporto(patio):
    espacos = 0

    for x, linha in enumerate(patio):
        y = linha.find('*')
        if y >= 0:
            entrada = (x, y)

    return ver(set(), patio, *entrada) - 1

    for linha in patio:
        espacos += andar_linha(linha)
        espacos += andar_linha(''.join(reversed(linha)))

    return espacos

def ver(vi, patio, x, y):
    if (x,y) in vi:
        return 0
    vi.add((x,y))

    return 1+(ver(vi, patio, x+1, y) +
              ver(vi, patio, x-1, y) +
              ver(vi, patio, x, y+1) +
              ver(vi, patio, x, y-1))

def andar_linha(linha):
    espacos = 0
    for lugar in linha[linha.find('*')+1:]:
            if lugar == "#":
                break
            if lugar != "*":
                espacos += 1
    return espacos
