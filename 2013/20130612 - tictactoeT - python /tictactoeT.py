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
	diagonal = ''
	outra_diagonal = ''
	for l in range(4):
		diagonal += entrada[l][l]
		outra_diagonal += entrada[l][3 - l]

	total = entrada + transpor(entrada) + [diagonal, outra_diagonal]

	for linha in total:
		ganhador = linha_preenchida_por_quem(linha)
		if ganhador:
			return ganhador + ' Ganhou'

	return 'Rolando'
