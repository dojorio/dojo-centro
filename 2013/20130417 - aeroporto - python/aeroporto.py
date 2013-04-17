#-*- coding: utf-8 -*-

def aeroporto(patio):
    espacos = 0

    for linha in patio:
        for lugar in linha:
            if lugar == "#":
                break
            if lugar != "*":
                espacos += 1

    return espacos
