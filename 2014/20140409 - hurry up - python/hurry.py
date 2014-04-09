def hurry(jogadores, chegadas):
    jx, jy, jv = jogadores[0]
    cx, cy = chegadas[0]
    return ((jx - cx)**2 + (jy - cy)**2)**1/2