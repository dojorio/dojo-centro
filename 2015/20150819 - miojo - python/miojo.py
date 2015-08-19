def tempo_minimo(ampulheta_1, ampulheta_2):
	if {1, 3} & {ampulheta_1, ampulheta_2}:
		return 3
	elif ampulheta_1 % 2 == 0 and ampulheta_2 % 2 == 0:
		return None
	elif ampulheta_2 == ampulheta_1:
		return None
	else:
		return max(ampulheta_1, ampulheta_2)
