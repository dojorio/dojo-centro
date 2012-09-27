#coding: utf-8

"""
0/3 = 0
1/3 = 0 (0.3333333)
2/3 = 0 (0.666666)

3/3 = 1
4/3 = 1 (1.333)
5/3 = 1 (1.66666)

6/3 = 2
"""

def clicar(tabuleiro, i, valor):
    tabuleiro[i] += valor
    
    if i % 3:
        tabuleiro[i-1] += valor
    if i % 3 != 2:
        tabuleiro[i+1] += valor
    if i / 3:
        tabuleiro[i-3] += valor
    if i / 3 != 2:
        tabuleiro[i+3] += valor

def numpuzz(tabuleiro):
    if not any(tabuleiro):
        return []
     
    for i in range(9):
        clicar(tabuleiro, i, -1)

        if not any(tabuleiro):
            return [i]
        
        result = numpuzz(tabuleiro)  
        
        if result:
            return [i] + result

        clicar(tabuleiro, i, +1)
