def menor_diferenca(doces):

    return min( 
            abs(sum(doces) - 2*max(doces)), 
            abs(sum(doces) - 2*(max(doces) + min(doces)))
            )