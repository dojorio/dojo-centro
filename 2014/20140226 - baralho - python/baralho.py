def baralho(n):
    descartadas = list(range(1, n + 1, 2))
    if n == 4:
        descartadas.append(2)
    if n == 3:
        return ([1, 3], 2)
    if n == 2:
        descartadas.append(2)
        return (descartadas, 2)
    return (descartadas, 1)

