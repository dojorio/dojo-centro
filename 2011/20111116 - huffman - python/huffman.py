import heapq

def frequencia(palavra):
    tabela = {}
    
    for caractere in palavra:
        tabela[caractere] = tabela.get(caractere, 0) + 1
    return tabela    

def merge(a, b):
    frequencia = a[0] + b[0]
    return (frequencia, None, a, b)

def prefixos(tabela):
    floresta = [(f, c) for c, f in tabela.items()]
    heapq.heapify(floresta)
    
    while len(floresta) > 1:
        esquerda = heapq.heappop(floresta);
        direita = heapq.heappop(floresta);
        pai = merge(esquerda, direita)
        heapq.heappush(floresta, pai)
    return floresta[0]    

    
    