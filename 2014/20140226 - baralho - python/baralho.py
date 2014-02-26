def baralho(n):
    descartadas = list(range(1, n + 1, 2))

    if n == 1:
        return ([],1)
    
    return (descartadas,n)

