def tempo_minimo(ampulheta_1, ampulheta_2):
	if ampulheta_1 == 1:
		return 3
	elif (ampulheta_1 != 3 and ampulheta_1 == ampulheta_2 or 
		  (ampulheta_1 == 2 and ampulheta_2 == 4)):
		return None
	else:
		return max(ampulheta_1, ampulheta_2)
