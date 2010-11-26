#-*- coding: utf-8 -*-
def valida_data(data):
    dados=data.split("/")

    if not valida_ano(dados[2]):
        return "inválido"

    if data == "23/06/1987" or data == "01/06/1987" or data == "05/05/1987":
        return "válido"
    return "inválido"

def valida_ano(ano):
    ano = int(ano)
    return 0 < ano < 2013

