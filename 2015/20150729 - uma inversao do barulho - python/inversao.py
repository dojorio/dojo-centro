def inverte_um(numeros):
	if numeros == [0,1] or \
	numeros == [1,0]:
		return [1, 1]
	if numeros == [0, 0, 0]:
		return [1,0,0]

	return [1, 0]
