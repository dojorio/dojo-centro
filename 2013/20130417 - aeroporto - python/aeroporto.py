#-*- coding: utf-8 -*-

def aeroporto(patio):
    espacos = 0

    for linha in patio:
        for lugar in linha[linha.find('*')+1:]:
            if lugar == "#":
                break
            espacos += 1
        if '*' in linha:
            outra_linha = ''.join(reversed(linha))
            for lugar in outra_linha[outra_linha.find('*')+1:]:
                if lugar == "#":
                    break
                espacos += 1

    return espacos

def andar_linha(linha):
    espacos = 0
    for lugar in linha[linha.find('*')+1:]:
            if lugar == "#":
                break
            espacos += 1
    return espacos
