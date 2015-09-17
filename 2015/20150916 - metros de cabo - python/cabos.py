from collections import Counter
def metros_de_cabo(grafo):
	


	pesos = [aresta[1] for aresta in grafo]
	vertices = sum((aresta[0] for aresta in grafo), tuple())
	vertices_unicos = set(vertices)
	minimo_de_arestas_necessarias = len(vertices_unicos) - 1
	total = sum(pesos)

	while minimo_de_arestas_necessarias < len(pesos):
		total -= pesos.pop(pesos.index(max(pesos)))

	return total
	