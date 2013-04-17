#-*- coding: utf-8 -*-

def aeroporto(patio):
    espacos = 0

    for linha in patio:
        for lugar in linha[linha.find('*'):]:
            if lugar == "#":
                break
            espacos += 1

    return espacos
