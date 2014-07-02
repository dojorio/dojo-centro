def pode_atacar(tabuleiro):
    for linha in tabuleiro:
        if (linha.count(1) >= 2):
            return True

    for j in xrange(0, 4):
        coluna = [linha[j] for linha in tabuleiro]
        if (coluna.count(1) >= 2):
            return True


    return False