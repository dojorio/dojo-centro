def metros_de_cabo(grafo):
	pesos = (aresta[1] for aresta in grafo)
	vertices_unicos = set(sum((aresta[0] for aresta in grafo), tuple()))
	if len(vertices_unicos) < len(grafo):
		return sum(pesos) - min(pesos)
	return sum(pesos)
	