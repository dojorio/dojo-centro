def pode_atacar(tabuleiro):
    for linha in tabuleiro:
        if (linha.count(1) >= 2):
            return True

    for j in xrange(0, 4):
        coluna = [linha[j] for linha in tabuleiro]
        if (coluna.count(1) >= 2):
            return True


    if(tabuleiro[0][0] == 1 and tabuleiro[1][1] == 1):
        return True

    if(tabuleiro[0][0] == 1 and tabuleiro[2][2] == 1):
        return True


    return False