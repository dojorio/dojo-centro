def corrida (pinoqui1, pinoqui2, pista):
    nariz = 1
    tamanho = 0

    if pinoqui1[tamanho] > pinoqui2[tamanho]:
        return 'pinoquio2'
    if pinoqui1[tamanho] < pinoqui2[tamanho]:
        return 'pinoquio1'

    if pinoqui1[nariz] > pinoqui2[nariz]:
        return 'pinoquio1'
    if pinoqui1[nariz] < pinoqui2[nariz]:
        return 'pinoquio2'

    return 'empate'
