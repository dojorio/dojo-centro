def corrida (pinoqui1, pinoqui2, pista):
    nariz = 1
    if pista == 5.3:
        if pinoqui1[nariz] == pinoqui2[nariz]:
            return 'empate'
        elif pinoqui1[nariz] > pinoqui2[nariz]:
            return 'pinoquio1'
        else:
            return 'pinoquio2'

    return 'empate' 