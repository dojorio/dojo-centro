def knight_escape(cavalo, peoes):
    possibilidades = 8
    coluna, linha = cavalo[0], cavalo[1]

    if coluna == 'a':
        possibilidades -= 4

        if linha in ('1', '8'):
            possibilidades -= 2

        if linha in ('2'):
            possibilidades -= 1

    return possibilidades

