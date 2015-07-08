def topo(saida,colunas):
	for c in range(colunas):

		saida [0][c] = c + 1
	return saida 

def espiral(colunas, linhas):
	saida=[]
	for l in range(linhas):
		saida.append([])
		for c in range(colunas):
			saida[l].append(0)
	print(linhas,colunas, saida)
	topo(saida,colunas)
	return saida
'''
if colunas == 2 and linhas == 3:
	return [[1,2], [6,3], [5,4]]
algo = []

for x in range(1, colunas+1):
	algo.append(x)

if linhas == 2:
	algo_mais = []
	for l in range(1, colunas+1):
		x += 1
		algo_mais.append(x)
	algo_mais.reverse()
	return [algo,algo_mais]

if linhas > 2:
	algo_menos = []
	for l in range(1, linhas+1):
		algo_menos.append([l])
	return algo_menos



return [algo]
'''