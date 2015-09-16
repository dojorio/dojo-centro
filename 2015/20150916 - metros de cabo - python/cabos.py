def metros_de_cabo(grafo):
	if len(grafo) == 2:
		return grafo[0][1] + grafo[1][1]
	return grafo[0][1]