def linhas_cruzadas(linha1, linha2):
	l1_p2_y = linha1[1][1]
	l2_p1_y = linha2[0][1]
	l1_p1_y	= linha1[0][1]
	l2_p1_y = linha2[0][1]


	if linha1[0] in linha2:
	    return True
	elif linha1[1] in linha2:
	    return True    
	elif l1_p2_y > l2_p1_y and l1_p1_y < l2_p1_y:
		return True
	elif linha1[1][0] > linha2[0][0] and linha1[0][0] < linha2[0][0]:
		return True
	elif linha1[1][1] >= linha2[1][1] and linha1[0][1] < linha2[1][1]:
		return True

	return False