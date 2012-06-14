# coding: utf-8
import re

def distancia(texto1, texto2):
    lista1 = tokenizar(texto1)
    lista2 = tokenizar(texto2)
    conta_operacao = 0
    
    for palavra1, palavra2 in zip(lista1, lista2):
        if palavra1 != palavra2:
            conta_operacao += 1

    return abs(len(lista1) - len(lista2)) + conta_operacao

def tokenizar(texto):
    return re.sub('[^\w]', u' ', texto, 0, re.UNICODE).split()
