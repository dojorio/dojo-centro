def menor_diferenca(doces, n_criancas = 2):
    doces.sort()
    criancas = [0] * n_criancas

    for doce in doces[::-1]:
        crianca = crianca_menos_doces(criancas)
        criancas[crianca] += doce

    return abs(max(criancas) - min(criancas))

def crianca_menos_doces(criancas):
    return criancas.index(min(criancas))

