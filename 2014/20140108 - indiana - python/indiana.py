def indiana(rampas, largura, altura):
	if len(rampas) == 2:
		return largura - min(rampas[1][1], rampas[0][1])
	else: 
		return largura - rampas[0][1]