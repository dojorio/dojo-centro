def knight_escape(cavalo, peoes):
    possibilidades = 8
    coluna, linha = cavalo[0], cavalo[1]

    if coluna in ('a','h'):
        possibilidades -= 4

        if linha in ('1', '8'):
            possibilidades -= 2

        if linha in ('2', '7'):
            possibilidades -= 1

    if coluna in ('b','g'):
        possibilidades -= 2

        if linha in ('1', '8'):
            possibilidades -= 3

        if linha in ('2', '7'):
            possibilidades -= 2

    if coluna in ('e', 'd', 'f', 'c'):
        possibilidades -= 0

        if linha in ('1', '8'):
            possibilidades -= 4

        if linha in ('2', '7'):
            possibilidades -= 2

    return possibilidades

