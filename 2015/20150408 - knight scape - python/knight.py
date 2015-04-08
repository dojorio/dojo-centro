def knight_escape(cavalo, peoes):
    if cavalo == 'c4':
        return 8

    if cavalo[0] == 'a':
        return int(cavalo[1]) + 1