from collections import Counter

def metros_de_cabo(grafo):
	vertices = sum((aresta[0] for aresta in grafo), tuple())
	graus_vertices = Counter(vertices)
	grafo.sort(key = lambda x: x[1], reverse = True)

	minimo_de_arestas_necessarias = len(graus_vertices) - 1
	total = sum(pesos)

	while minimo_de_arestas_necessarias < len(grafo):
		total -= pesos.pop(pesos.index(max(pesos)))
		

	return total
	