# -*- coding: utf-8 -*-
def roleta(numero_de_pessoas, passo):
    if passo == 1:
        return numero_de_pessoas
    if numero_de_pessoas == 1:
        return 1
    if passo == 2:
        if numero_de_pessoas == 3:
           return 3
        return 1
    if passo == 3:
        if numero_de_pessoas == 4:
            return 4
        return 2

    if passo == 4:
        return 1

    return numero_de_pessoas

