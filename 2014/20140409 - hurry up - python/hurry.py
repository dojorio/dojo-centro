def hurry(jogadores, chegadas):
    jx, jy, jv = jogadores[0]
    def distancia(x, y):
        return ((jx - x)**2 + (jy - y)**2)**.5
    
    return min(distancia(x, y)/jv for x, y in chegadas)
    