def indiana(rampas, largura, altura):
	espacos = []

	for i, rampa in enumerate(rampas):
		if i % 2 == 0:
			espacos.append(largura - rampa[1])
		else:
			espacos.append(rampa[1])

	return min(espacos)