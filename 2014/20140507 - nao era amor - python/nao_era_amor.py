MULTIPLICADORES = {
    '+': 1,
    '-': -1,
    '.': 0
}

def cilada(tabuleiro, padrões):

    resultados_possíveis = []

    for padrão in padrões:
        resultados_possíveis.append(
            tabuleiro[0][0] * MULTIPLICADORES[padrão])

    return max(resultados_possíveis)