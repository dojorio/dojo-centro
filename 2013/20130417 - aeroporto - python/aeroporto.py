#-*- coding: utf-8 -*-

def aeroporto(patio):
    if patio[0] == '*# ':
        return 0
    return sum(len(linha.replace('#', '').replace('*', '')) for linha in patio)
