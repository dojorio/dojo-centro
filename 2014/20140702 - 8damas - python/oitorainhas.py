def pode_atacar(tabuleiro):
    if (tabuleiro[0].count(1) >= 2):
        return True
    if (tabuleiro[1].count(1) >= 2):
        return True
    if (tabuleiro[2].count(1) >= 2):
        return True
    if (tabuleiro[3].count(1) >= 2):
        return True
    return False