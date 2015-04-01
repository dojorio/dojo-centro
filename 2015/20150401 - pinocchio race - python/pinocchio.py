def corrida (pinoqui1, pinoqui2, pista):
    nariz = 1
    tamanho = 0

    dist1 = 5.0/pinoqui1[tamanho] + pinoqui1[nariz]
    dist2 = 5.0/pinoqui2[tamanho] + pinoqui2[nariz]

    if dist1 > dist2:
        return 'pinoquio1'
    if dist1 < dist2:
        return 'pinoquio2'

    return 'empate'
