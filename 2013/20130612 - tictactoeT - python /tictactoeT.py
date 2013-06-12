def linha_preenchida_por(linha, jogador):
	return linha.count('T') + linha.count(jogador) == 4

def linha_preenchida_por_quem(linha):
	if linha_preenchida_por(linha, 'x'):
		return 'x'
	elif linha_preenchida_por(linha, 'o'):
		return 'o'

def coluna_preenchida_por(coluna, jogador):
	return coluna.count('T') + coluna.count(jogador) == 4

def transposta(entrada):
	transposta_da_entrada = []
	for linha in entrada:
		colu
	return transposta_da_entrada

def verifica(entrada):

	for linha in entrada:
		ganhador = linha_preenchida_por_quem(linha)
		if ganhador:
			return ganhador + ' Ganhou'


	coluna0 = entrada[0][0] + entrada[1][0] + entrada[2][0] + entrada[3][0]
	ganhador = linha_preenchida_por_quem(coluna0)
	if ganhador:
			return ganhador + ' Ganhou'
	return 'Rolando'
