def identifica_padrao(danca):
    tamanho_minimo_do_padrao = len(danca)/3
    tamanho_maximo_do_padrao = len(danca)/2 + 1
    
    for i in xrange(tamanho_minimo_do_padrao, tamanho_maximo_do_padrao):
        padrao = danca[:i]
        if (padrao * 3)[:len(danca)] == danca:
            return padrao
            
def proximos_n(danca, n=8):
    padrao = identifica_padrao(danca)
    return ''.join(padrao[i % len(padrao)] for i in xrange(len(danca), len(danca)+n))

