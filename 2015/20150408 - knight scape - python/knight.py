def knight_escape(cavalo, peoes):
    possibilidades = 0
    if cavalo == 'c4':
        possibilidades = 8

    if cavalo[0] == 'a':
        possibilidades =  int(cavalo[1]) + 1
    return possibilidades 