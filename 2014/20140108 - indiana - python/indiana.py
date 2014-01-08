def indiana(rampas, largura, altura):
	espacos = []
	espacos.append(largura - rampas[0][1])

	if len(rampas) == 2:
		espacos.append(rampas[1][1])

	return min(espacos)