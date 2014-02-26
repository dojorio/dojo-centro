def baralho(tamanho_baralho):
    deck = list(range(1, tamanho_baralho + 1))
    cemiterio = []
    impar = True

    while len(deck) > 1:
        primeiro = deck.pop(0)
        if impar:
            cemiterio.append(primeiro)
        else:
            deck.append(primeiro)
        impar = not impar

    return (cemiterio, deck[0])
