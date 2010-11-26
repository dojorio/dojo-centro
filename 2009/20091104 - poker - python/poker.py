# -*- coding: utf-8 -*-
def poker(mao1, mao2):
    
    cartas_mao1 = [int(x[:-1]) for x in mao1.split()]
    cartas_mao2 = [int(x[:-1]) for x in mao2.split()]
    if jogo(cartas_mao1) > jogo(cartas_mao2):
        return "Mao 1 (%s) ganha da Mao 2 (%s)" % (mao1, mao2)
    elif max(cartas_mao1) > max(cartas_mao2):
        return "Mao 1 (%s) ganha da Mao 2 (%s)" % (mao1, mao2)

    return "Mao 2 (%s) ganha da Mao 1 (%s)" % (mao2, mao1)
    
def jogo(cartas_mao):
    par = None
    trinca = None
    
    maximo = 0
    for i in range(2, 15):
        if cartas_mao.count(i) * 100 + i > maximo:
           maximo = cartas_mao.count(i) * 100 + i
    return maximo  