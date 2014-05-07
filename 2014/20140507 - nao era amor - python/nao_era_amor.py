MULTIPLICADORES = {
    '+': 1,
    '++': 1.5, #ladrão
    '-+': -0.5,
    '-': -1,
    '.': 0
}

def valor(num, op):
    return num * MULTIPLICADORES[op]

def cilada(tabuleiro, padrões):

    resultados_possíveis = []

    for padrão in padrões:
        for linha in tabuleiro:
                resultados_possíveis.append(
                    sum(map(valor, zip(linha, padrão)))
                )

    return max(resultados_possíveis)