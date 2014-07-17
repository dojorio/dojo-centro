def menor_diferenca(doces, n_criancas = 2):
    doces.sort()
    criancas = [0] * n_criancas

    for doce in doces[::-1]:
        crianca = crianca_menos_doces(criancas)
        criancas[crianca] += doce

    if n_criancas == 3:
        return min(abs(criancas[0] - criancas[1]),
                   abs(criancas[1] - criancas[2]),
                   abs(criancas[0] - criancas[2]))
    else:
        return abs(criancas[0] - criancas[1])

def crianca_menos_doces(criancas):
    return criancas.index(min(criancas))

