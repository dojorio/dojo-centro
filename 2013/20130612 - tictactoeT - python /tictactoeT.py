def linha_preenchida_por(linha, jogador):
	return linha.count('T') + linha.count(jogador) == 4

def linha_preenchida_por_quem(linha):
	if linha_preenchida_por(linha, 'x'):
		return 'x'
	elif linha_preenchida_por(linha, 'o'):
		return 'o'

def verifica(entrada):

	for linha in entrada:
		ganhador = linha_preenchida_por_quem(linha)
		if ganhador:
			return ganhador + ' Ganhou'

	if entrada[3][0] == 'x':
		return 'x Ganhou'
	if entrada[3][0] == 'o':
		return 'o Ganhou'


	return 'Rolando'
