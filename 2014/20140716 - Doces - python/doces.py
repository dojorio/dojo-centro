def menor_diferenca(doces):
    if len(doces) <= 3:
        return abs(sum(doces) - 2*max(doces))
    
    return abs(sum(doces) - 2*(max(doces) + min(doces)))