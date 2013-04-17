#-*- coding: utf-8 -*-

def aeroporto(patio):
    espacos = 0

    for linha in patio:
        espacos += andar_linha(linha)
        espacos += andar_linha(''.join(reversed(linha)))


    return espacos

def andar_linha(linha):
    espacos = 0
    for lugar in linha[linha.find('*')+1:]:
            if lugar == "#":
                break
            espacos += 1
    return espacos
