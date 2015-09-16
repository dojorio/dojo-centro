def metros_de_cabo(grafo):
	pesos = (aresta[1] for aresta in grafo)
	vertices_unicos = set(sum((aresta[0] for aresta in grafo), tuple()))
	if len(vertices_unicos) - 1< len(grafo):
		return sum(pesos) - max(pesos)
	return sum(pesos)
	