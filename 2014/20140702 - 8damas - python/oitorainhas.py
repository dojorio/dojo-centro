def pode_atacar(tabuleiro):
    for linha in tabuleiro:
        if (linha.count(1) >= 2):
            return True

    for j in xrange(0, 4):
        coluna = [linha[j] for linha in tabuleiro]
        if (coluna.count(1) >= 2):
            return True
    acumulador_de_damas = 0
    for j in xrange(0, 4):
        if(tabuleiro[j][j] == 1):
            acumulador_de_damas += 1
    return acumulador_de_damas > 0