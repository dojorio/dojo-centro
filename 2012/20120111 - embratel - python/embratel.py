from math import sqrt

def comprimento_fibra_minimo(clientes):
    distancias_clientes = distancias(clientes)
    numero_de_links = len(clientes) - 1
    candidatos = list(distancias_clientes[0])
    menor_distancia = 1000000
    for i in range(numero_de_links):
        for j in range(numero_de_links):
            if candidatos[j] < menor_distancia:
                menor_distancia = candidatos[j]
           
                

def distancia(A, B):
    return sqrt((A[0]-B[0])**2+(A[1]-B[1])**2)
    
def distancias(clientes):
    todas_distancias = (
                    lambda A: tuple(map(lambda B: distancia(A,B), clientes))
                        )
    return tuple(map(todas_distancias, clientes))

 