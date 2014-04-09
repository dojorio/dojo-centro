def hurry(jogadores, chegadas):
    jx, jy, jv = jogadores[0]
    menor = 1000
    for cx, cy in chegadas:
        distancia = ((jx - cx)**2 + (jy - cy)**2)**.5
        tempo = distancia/jv
        menor = min (menor, tempo)
    return menor