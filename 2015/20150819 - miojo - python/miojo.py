def tempo_minimo(ampulheta_1, ampulheta_2):
	if {1, 3} & {ampulheta_1, ampulheta_2}:
		return 3
	elif ampulheta_1 % 2 == 0 and ampulheta_2 % 2 == 0:
		return None
	elif ampulheta_2 == ampulheta_1:
		return None

	maior = max(ampulheta_1, ampulheta_2)
	menor = min(ampulheta_1, ampulheta_2)

	if maior - menor == 3:
		return maior
	else:
		return menor * 2
