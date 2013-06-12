def linha_preenchida_por(linha, jogador):
	return linha.count('T') + linha.count(jogador) == 4

def verifica(entrada):
	if linha_preenchida_por(entrada[0], 'x'):
		return 'x Ganhou'
	if linha_preenchida_por(entrada[0], 'o'):
		return 'o Ganhou'
	return 'Rolando'
