def tempo(jogador, chegada):
    jx, jy, jv = jogador
    cx, cy = chegada
    return distancia(jx, jy, cx, cy )/jv

def distancia(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**.5

def hurry(jogadores, chegadas):
    
    return max(min(tempo(jogador, chegada) for chegada in chegadas)
                                           for jogador in jogadores)
