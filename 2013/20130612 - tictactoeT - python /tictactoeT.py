def linha_preenchida_por(linha, jogador):
	return linha.count('T') + linha.count(jogador) == 4

def linha_preenchida_por_quem(linha):
	if linha_preenchida_por(linha, 'x'):
		return 'x'
	elif linha_preenchida_por(linha, 'o'):
		return 'o'

def coluna_preenchida_por(coluna, jogador):
	return coluna.count('T') + coluna.count(jogador) == 4

def transpor(entrada):
	transposta = []
	for c in range(4):
		coluna = ''
		for l in range(4):
			coluna += entrada[l][c]
		transposta.append(coluna)
	return transposta


def verifica(entrada):
	total = entrada + transpor(entrada)
	for linha in total:
		ganhador = linha_preenchida_por_quem(linha)
		if ganhador:
			return ganhador + ' Ganhou'

	for linha in transpor(entrada):
		ganhador = linha_preenchida_por_quem(linha)
		if ganhador:
			return ganhador + ' Ganhou'

	return 'Rolando'
