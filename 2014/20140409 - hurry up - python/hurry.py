from itertools import permutations

def tempo(jogador, chegada):
    jx, jy, jv = jogador
    cx, cy = chegada
    return distancia(jx, jy, cx, cy )/jv

def distancia(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**.5

def hurry(jogadores, chegadas):
    arranjos = permutations(chegadas,len(jogadores))
           # melhor arranjo jogador-chegada
    return min(# tempo_maximo_deste_arranjo
               max(tempo(jogador,chegada) 
                   for jogador, chegada in zip(jogadores, arranjo))
               for arranjo in arranjos)
