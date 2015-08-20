def tempo_minimo(ampulheta_1, ampulheta_2):
	if (ampulheta_1, ampulheta_2) == (1, 1):
		return 3
	elif 3 in (ampulheta_1, ampulheta_2):
		return 3
	elif ampulheta_1 % 2 == 0 and ampulheta_2 % 2 == 0:
		return None
	elif ampulheta_2 == ampulheta_1 and ampulheta_1 > 3:
		return None

	maior = max(ampulheta_1, ampulheta_2)
	menor = min(ampulheta_1, ampulheta_2)

	diff = maior - menor
	if diff == 3:
		return maior
	elif menor * 2 < diff:
		return menor + tempo_minimo(menor, diff)
	else:
		return tempo_minimo(maior, menor * 2)
