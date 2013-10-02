def quantos_movimentos(patio):
    gabarito = sorted(patio)
    movimentos = 0
    for i, container in enumerate(patio):
        certo = gabarito[i]
        if container != certo:
            movimentos += 1
            i_do_certo = patio.index(certo)
            patio[i], patio[i_do_certo] = patio[i_do_certo], patio[i]


    if patio == sorted(patio):
        return 0
    return patio[:-1] + 1        


    return movimentos