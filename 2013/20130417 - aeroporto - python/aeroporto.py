#-*- coding: utf-8 -*-

def aeroporto(patio):
    espacos = 0

    for x, linha in enumerate(patio):
        y = linha.find('*')
        if y >= 0:
            entrada = (x, y)

    return ver_a_partir_de(patio, *entrada)

    for linha in patio:
        espacos += andar_linha(linha)
        espacos += andar_linha(''.join(reversed(linha)))

    return espacos

def ver_a_partir_de(patio, x, y):


    pass

def andar_linha(linha):
    espacos = 0
    for lugar in linha[linha.find('*')+1:]:
            if lugar == "#":
                break
            if lugar != "*":
                espacos += 1
    return espacos
