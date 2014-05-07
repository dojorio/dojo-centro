def cilada(tabuleiro, padrões):
    if padrões[0][0] == '+':
        multiplicador = 1
    else:
        multiplicador = -1

    return tabuleiro[0][0] * multiplicador