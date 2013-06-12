def verifica(entrada):

	if entrada[0].count('T') + entrada[0].count('x') == 4: return 'x Ganhou'
	if entrada[0].count('T') + entrada[0].count('o') == 4: return 'o Ganhou'
	return 'Rolando'
