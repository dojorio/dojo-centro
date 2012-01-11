# coding:utf-8
from collections import defaultdict

def agrupar(dados, coluna="Nome Município"):
    grupos = defaultdict(int)
    for item in dados:
        grupos[item[coluna]] += item["Valor"]
        
    return grupos
        