def campominado(tabuleiro):
    linha = tabuleiro[0]

    for indice, casa in enumerate(linha):
        if casa == '.':
            casa = '0'
        elif casa == '*':
            if indice > 0:
                linha[indice - 1] = '1'
            elif indice < len(linha) - 1:
                linha[indice + 1] = '1'

    if (len(linha) == 1):
        if linha[0] == '.':
            return [['0']]
        else:
            return tabuleiro

    if (len(linha) == 2):
        if linha == ['.','.']:
            return [['0','0']]


        for indice, casa in enumerate(linha):
            if casa == '.':
                linha[indice]='1'

        return [linha]


    return tabuleiro
