B = 'Branca'
P = 'Preta'

def definir_possiveis_jogadas(jogador, estado_do_jogo):
		if estado_do_jogo[0][2] == B:
			return [[0,1,B,1],
					[0,B,B,0],
					[0,P,B,1],
					[0,0,0,0]]
					
		if jogador == P:
			p = 1
			b = 0
		if jogador == B:
			p = 0
			b = 1
			
		for linha in range(0,len(estado_do_jogo)-1):
			for coluna in range(0,len(estado_do_jogo[linha])-1):
				print("faltou algo")
		return  [[0,p,b,0],
				 [p,B,P,b],
				 [b,P,B,p],
				 [0,b,p,0]] 