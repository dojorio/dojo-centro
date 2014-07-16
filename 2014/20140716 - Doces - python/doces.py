def menor_diferenca(doces):
    if len(doces) <= 3:
        return abs(sum(doces) - 2*max(doces))
    return max(doces)-min(doces)