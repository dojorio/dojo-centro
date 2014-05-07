MULTIPLICADORES = {
    '+': 1,
    '++': 1.5,
    '-': -1,
    '.': 0
}

def cilada(tabuleiro, padrões):

    resultados_possíveis = []

    for padrão in padrões:
        for linha in tabuleiro:
                resultados_possíveis.append(
                    linha[0] * MULTIPLICADORES[padrão])

    return max(resultados_possíveis)