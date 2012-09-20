#coding: utf-8

def numpuzz(passos, lado=3):
    area = lado*lado
    resultado = [0]*area
    
    def adicionar(posicao):
        if 0 <= posicao < area:
            resultado[posicao] += 1
            resultado[posicao] %= 10

    for passo in passos:
        esquerda = passo - 1
        direita = passo + 1
        cima = passo - lado
        baixo = passo + lado
        
        adicionar(passo)
        adicionar(cima)
        adicionar(baixo)
           
        if passo % lado:
            adicionar(esquerda)

        if (passo + 1) % lado:
            adicionar(direita)

    return resultado
    

