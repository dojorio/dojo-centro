def demarcar(flor, demarcacao):
#	distancia + raio_da_flor <= raio_demarcado
	return ((flor[1][0] - demarcacao[1][0])**2 - (flor[1][1] - demarcacao[1][1])**2)**0.5 <= raio_demarcacao[0]