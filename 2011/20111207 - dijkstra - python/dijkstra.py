def atualizar_se_menor(tabela, no, valor):
    if no not in tabela or valor < tabela[no]:
        tabela[no] = valor

def dijkstra(grafo, origem):
    tabela = {origem: 0}
    
    INF = 10000000
    
    for distancia, vizinho in grafo[origem]:
        atualizar_se_menor(tabela, vizinho, distancia)

        for distancia2, vizinho2 in grafo[vizinho]:
            atualizar_se_menor(tabela, vizinho2, distancia+distancia2)
            
            for distancia3, vizinho3 in grafo[vizinho2]:
                atualizar_se_menor(tabela, vizinho3, distancia+distancia2+distancia3)
    
    return tabela
    