MULTIPLICADORES = {
    '+': 1,
    '-': -1,
    '.': 0
}

def cilada(tabuleiro, padrões):
    resultado = 0

    for padrão in padrões:
        for linha in tabuleiro:
            for numero, operador in zip(linha, padrão):
                resultado += numero * MULTIPLICADORES[operador]

    return resultado