def baralho(tamanho_baralho):
    deck = list(range(1, tamanho_baralho + 1))
    descarte = []
    descartar = True

    while len(deck) > 1:
        primeiro = deck.pop(0)
        if descartar:
            descarte.append(primeiro)
        else:
            deck.append(primeiro)
        descartar = not descartar

    return (descarte, deck[0])
