# coding: utf-8

def troco(valor, valores = [100, 50, 20, 10, 5, 2, 1, .50, .25], indice_ultima = 0):
    if indice_ultima >= len(valores):
        return None
    
    if valor < 0: 
        return None
    
    if valor == 0: 
        return []
    
    if len(valores) == 0: 
        return None

    pre_resultado1 = troco(valor-valores[indice_ultima], valores, indice_ultima)

    if pre_resultado1 != None:
        resultado1 = [valores[indice_ultima]] + pre_resultado1
    else:
        resultado1 = None
    
    resultado2 = troco(valor, valores, indice_ultima+1)

    if resultado2 == None or resultado1 != None and len(resultado1) < len(resultado2):
        return resultado1
    else:
        return resultado2

