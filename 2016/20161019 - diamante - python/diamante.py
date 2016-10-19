def diamante(letra):
	diamantes = {
		'A': ['A'],
		'B': [' A ', 'B B',' A '],
		'C': ['  A  ', ' B B ', 'C   C', ' B B ', '  A  ']
	}

	return diamantes[letra]