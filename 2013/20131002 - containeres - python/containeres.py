def quantos_movimentos(patio):
    gabarito = sorted(patio)
    movimentos = 0    
    while patio != gabarito:
        for i in range(len(patio)-1):
            if patio[i] > patio[i+1]:
                movimentos += 1
                patio[i], patio[i+1] = patio[i+1], patio[i]

    return movimentos