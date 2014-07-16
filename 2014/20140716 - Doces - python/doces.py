def menor_diferenca(doces):
    # return min( 
    #         abs(sum(doces) - 2*max(doces)), 
    #         abs(sum(doces) - 2*(max(doces) + min(doces))),
    #         abs(sum(doces) - 2*(max(doces) + min(doces)+2)),
    #         )

    criancas = [0, 0]
    for doce in doces:
        if criancas[0] > criancas[1]:
            criancas[1] += max(doces)
        else:
            criancas[0] += max(doces)
        doces.remove(max(doces))
    return abs(criancas[0] - criancas[1]
