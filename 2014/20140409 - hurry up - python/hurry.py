def hurry(jogadores, chegadas):
    jx, jy, jv = jogadores[0]
    cx, cy = chegadas[0]
    return abs(jx + jy - (cx + cy))