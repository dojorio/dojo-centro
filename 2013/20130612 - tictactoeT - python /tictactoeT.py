def verifica(entrada):

	if entrada[0].count('T') == 1:
	 	if entrada[0].count('x') <3 and entrada[0].count('o') <3:
			return 'Rolando'
	elif entrada[0].count('x') <4 and entrada[0].count('o') <4:
		return 'Rolando'

	return entrada[0][1] + ' Ganhou'
