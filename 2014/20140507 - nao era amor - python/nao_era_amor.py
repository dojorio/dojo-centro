MULTIPLICADORES = {
    '+': 1,
    '-': -1,
    '.': 0
}

def cilada(tabuleiro, padrões):
    
    resultados_possiveis = []

    for padrão in padrões:
        for linha in tabuleiro:
            resultado = 0
            for numero, operador in zip(linha, padrão):
                resultado += numero * MULTIPLICADORES[operador]

            resultados_possiveis.append(resultado)

    return max(resultados_possiveis)