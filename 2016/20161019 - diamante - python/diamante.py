def diamante(letra):
	result = []
	n_colunas = (2 * ord(letra) - ord('A')) + 1
	for l in range(ord('A'), ord(letra)):
		distancia_ate_a = ord(l) - ord('A')
		meio = n_colunas / 2 
		
		linha = ' ' * n_colunas
		linha[meio - distancia_ate_a] = chr(l)
		linha[-(meio - distancia_ate_a)] = chr(l)	
		result.append(linha)

	return result