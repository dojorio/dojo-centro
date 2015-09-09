def linhas_cruzadas(linha1, linha2):
	if linha1[0] in linha2:
	    return True
	elif linha1[1] in linha2:
	    return True

	return False