def linha_preenchida_por(linha, jogador):
	return linha.count('T') + linha.count(jogador) == 4

def linha_preenchida_por_quem(linha):
	if linha_preenchida_por(linha, 'x'):
		return 'x'
	elif linha_preenchida_por(linha, 'o'):
		return 'o'



def verifica(entrada):
	ganhador = linha_preenchida_por_quem(entrada[0])
	if ganhador:
		return ganhador + ' Ganhou'

	return 'Rolando'
