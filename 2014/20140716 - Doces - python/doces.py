def menor_diferenca(doces, criancas = 2):
    doces.sort()
    criancas = [0] * criancas

    for doce in doces[::-1]:
        crianca = crianca_menos_doces(criancas)
        criancas[crianca] += doce

    if criancas == 3:
        return criancas
    else:
        return abs(criancas[0] - criancas[1])

def crianca_menos_doces(criancas):
    return criancas.index(min(criancas))

