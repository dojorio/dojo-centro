def menor_diferenca(doces):
    if len(doces) == 1:
        return doces[0]
    else:
        return max(doces) - min(doces)