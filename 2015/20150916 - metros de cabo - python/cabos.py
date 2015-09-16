def metros_de_cabo(grafo):
	pesos = (aresta[1] for aresta in grafo)
	return sum(pesos)
	