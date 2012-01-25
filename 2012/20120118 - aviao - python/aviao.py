from random import choice

def escolhe_assento_vago(embarcados, passageiro):
    assentos_vagos = []
    for i, assento in enumerate(embarcados):
        if assento == 0:
            assentos_vagos.append(i)
    embarcados[choice(assentos_vagos)] = passageiro
    return embarcados
                    
def embarcar(quantidade_passageiros):
    embarcados = [0] * quantidade_passageiros
    escolhe_assento_vago(embarcados, 1)

    for passageiro in range(2, quantidade_passageiros+1):
        if embarcados[passageiro-1] == 0:
            embarcados[passageiro-1] = passageiro
        else:
            escolhe_assento_vago(embarcados, passageiro)   

    return embarcados

