def pode_atacar(tabuleiro):
    for linha in tabuleiro:
        if (linha.count(1) >= 2):
            return True

    if tabuleiro[0][0] == 1 and tabuleiro[1][0] == 1:
        return True


    return False