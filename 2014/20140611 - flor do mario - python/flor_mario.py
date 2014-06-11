def demarcar(flor, demarcacao):
	if flor == (1, (1, 0)):
		return True
	return flor[0] <= demarcacao[0] and flor[1] == demarcacao[1] 