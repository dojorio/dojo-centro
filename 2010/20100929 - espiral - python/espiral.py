#-*- coding: utf-8 -*-

def espiral(linhas, colunas):
    quantidade_de_elementos = linhas * colunas
    casas = len(str(quantidade_de_elementos))

    if linhas == 1:
        return ' '.join(map(str, range(1, quantidade_de_elementos + 1 )))


    primeira_metade = range(1, quantidade_de_elementos/2 + 1)
    primeira_metade = " ".join([str(valor).rjust(casas) for valor in primeira_metade])

    segunda_metade = range(quantidade_de_elementos, quantidade_de_elementos/2, -1)
    segunda_metade = " ".join([str(valor).rjust(casas) for valor in segunda_metade])

    return primeira_metade + "\n" + segunda_metade

