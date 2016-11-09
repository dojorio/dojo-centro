def diamante(letra):
	result = []
	n_colunas = 2 * (ord(letra) - ord('A')) + 1
	meio = n_colunas // 2
	for l in range(ord('A'), ord(letra) + 1):
		distancia_ate_a = l - ord('A')
		linha = [' '] * n_colunas
		linha[meio - distancia_ate_a] = chr(l)
		linha[-(meio - distancia_ate_a) -1] = chr(l)	
		result.append(''.join(linha))

	result = result + result[:-1][::-1]
	return result