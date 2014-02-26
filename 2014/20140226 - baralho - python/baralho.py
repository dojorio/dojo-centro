def baralho(tamanho_baralho):
    if tamanho_baralho == 1:
        return ([],1)

    descartadas = list(range(1, tamanho_baralho + 1, 2))

    if tamanho_baralho == 4:
        descartadas.append(2)
    
    n = max(range(0, tamanho_baralho + 1, 2))

    return (descartadas, n)

