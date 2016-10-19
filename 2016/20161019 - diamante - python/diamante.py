def diamante(letra):
	if letra == 'B':
		return [
			' A ',
			'B B',
			' A ',
		]
	if letra == 'C':
		return [ 
			'  A  ',
			' B B ',
			'C   C',
			' B B ',
			'  A  ',
		]
	return ['A']