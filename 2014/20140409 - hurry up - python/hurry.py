from itertools import permutations

def tempo(jogador, chegada):
    jx, jy, jv = jogador
    cx, cy = chegada
    return distancia(jx, jy, cx, cy )/jv

def distancia(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**.5

def hurry(jogadores, chegadas):
    arranjos = permutations(chegadas,len(jogadores))

    min_global = 10000
    for arranjo in arranjos:
        max_local = 0
        for jogador, chegada in zip(jogadores, arranjo):
            max_local = max(max_local, tempo(jogador, chegada))

        min_global = min(min_global, max_local)
    return min_global


    return min(max(tempo(jogador,chegada) 
        for jogador,chegada in zip(jogadores,arranjo)

        ) for arranjo in arranjos
        )
