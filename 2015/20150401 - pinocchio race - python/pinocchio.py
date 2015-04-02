
def corrida (pinoqui1, pinoqui2, pista):
    nariz = 1
    tamanho = 0

    v = lambda pinoquio: 5.0/pinoquio[tamanho]

    dist1 = v(pinoqui1) + pinoqui1[nariz]
    dist2 = v(pinoqui2) + pinoqui2[nariz]

    if dist1 > dist2:
        return 'pinoquio1'
    if dist1 < dist2:
        return 'pinoquio2'

    return 'empate'
