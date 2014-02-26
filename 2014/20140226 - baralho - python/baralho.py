def baralho(tamanho_baralho):
    if tamanho_baralho == 1:
        return ([],1)

    baralho_completo = list(range(1, tamanho_baralho + 1))
    descartadas = list(range(1, tamanho_baralho + 1, 2))

    return (descartadas, n)

