def linhas_cruzadas(linha1, linha2):
	l1_p1_x	= linha1[0][0]
	l1_p1_y	= linha1[0][1]
	l1_p2_x = linha1[1][0]
	l1_p2_y = linha1[1][1]

	l2_p1_x = linha2[0][0]
	l2_p1_y = linha2[0][1]
	l2_p2_x = linha2[1][0]	
	l2_p2_y = linha2[1][1]

	if linha1[0] in linha2:
	    return True
	elif linha1[1] in linha2:
	    return True    
	elif l1_p2_y > l2_p1_y and l1_p1_y < l2_p1_y and l2_p1_x == l1_p1_x:
		return True
	elif l1_p2_x > l2_p1_x and l1_p1_x < l2_p1_x and l2_p1_y == l1_p1_y:
		return True
	elif l1_p2_x > l2_p2_x and l1_p1_x < l2_p2_x and l2_p1_y == l1_p1_y:
		return True
	elif l1_p2_y > l2_p2_y and l1_p1_y < l2_p2_y and l2_p1_x == l1_p1_x:
		return True

	if l1_p2_y > l2_p1_y and l1_p1_y < l2_p1_y and l2_p1_x < l1_p1_x:
		return True

	return False