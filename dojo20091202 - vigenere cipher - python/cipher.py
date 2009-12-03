# -*- coding: utf-8 -*-

def criptografa(texto_original, chave):
    alpha = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
    hash = ""
    for caracter in texto_original:
        hash += alpha[alpha.find(caracter) + alpha.find(chave)]
    return hash
