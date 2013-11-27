def cards(cartas):
    if len(cartas) == 0:
        return 0

    return max(
        cartas[0] + sum(cartas[1:]) - cards(cartas[1:]),
        cartas[-1] + sum(cartas[:-1]) - cards(cartas[:-1]))

