def findmin(vetor, e, d):
    visao = vetor[e:d]
    return e + visao.index(min(visao))

def escalar(montanha, e = 0, d = None):
    if len(montanha) == 0:
        return []

    nivel = montanha[-1]
    minimo = 100000
    resposta_minima = []

    for indice in range(e, d or len(nivel)):
        e, d = max(indice - 1, 0), min(indice + 2, len(nivel))
        resposta = [indice + 1] + escalar(montanha[:-1], e, d)
        perigo = sum(montanha[-i-1][j-1] for i, j in enumerate(resposta))

        if valor < minimo:
            minimo = valor
            resposta_minima = resposta

    return resposta_minima    
