def verificar_triangulo_possivel(n, x, y, triangulo):
	direita = True
	esquerda = True

	for i in range(n):
		if not triangulo[x + n - i - 1][y:].startswith('-'*(i*2+1)):
			esquerda = False
	
	for i in range(n):
		if not triangulo[n - i - 1].endswith('-'*(i*2+1)):	
			direita = False

	return esquerda or direita

def star(triangulo):
	for i in range(len(triangulo), 0, -1):
		if verificar_triangulo_possivel(i, triangulo):
			return i*i
	return 0