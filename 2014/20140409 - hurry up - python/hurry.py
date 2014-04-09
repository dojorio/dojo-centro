def hurry(jogadores, chegadas):
    jx, jy, jv = jogadores[0]
    cx, cy = chegadas[0]
    distancia = ((jx - cx)**2 + (jy - cy)**2)**.5
    tempo = distancia/jv
    return tempo