def menor_diferenca(doces):
    if len(doces) <= 3 or max(doces) == 5:
        return abs(sum(doces) - 2*max(doces))
    
    return abs(sum(doces) - 2*(max(doces) + min(doces)))