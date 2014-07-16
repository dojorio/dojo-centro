def menor_diferenca(doces):
    if len(doces) == 1:
        return doces[0]
    elif len(doces) == 2:
        return max(doces) - min(doces)
    else:
        return 2*max(doces) - sum(doces)