#coding: utf-8

def gattaca(pai, mae):
    
    if len(pai) == 4:
        prob0 = dominante(pai[0:2], mae[0:2]) * dominante(pai[2:4], mae[2:4])
        prob2 = recessivo(pai[0:2], mae[0:2]) * recessivo(pai[2:4], mae[2:4])

        prob1 = 1 - (prob0 + prob2)
        return [prob0, prob1, prob2]
    
    return [dominante(pai, mae), recessivo(pai, mae)]

def dominante(pai, mae):
    return 1 - recessivo(pai, mae)

def recessivo(pai, mae):
    return (pai.count('a')/2.0) * (mae.count('a')/2.0)