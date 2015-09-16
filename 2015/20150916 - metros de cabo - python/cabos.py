def metros_de_cabo(grafo):
	pesos = [aresta[1] for aresta in grafo]
	vertices = sum((aresta[0] for aresta in grafo), tuple())
	vertices_unicos = set(vertices)
	minimo_de_arestas_necessarias = len(vertices_unicos) -1

	if minimo_de_arestas_necessarias < len(grafo):
		return sum(pesos) - max(list(pesos))
	return sum(pesos)
	