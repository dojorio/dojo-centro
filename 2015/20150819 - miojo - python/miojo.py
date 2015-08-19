def tempo_minimo(ampulheta_1, ampulheta_2):
	if ampulheta_1 == 3:
		return 3
	if ampulheta_1 == ampulheta_2:
		return None
	return max(ampulheta_1, ampulheta_2)
