def menor_diferenca(doces, criancas = 2):
    doces.sort()
    criancas = [0, 0]
    for doce in doces[::-1]:
        if criancas[0] > criancas[1]:
            criancas[1] += doce
        else:
            criancas[0] += doce
    return abs(criancas[0] - criancas[1])
