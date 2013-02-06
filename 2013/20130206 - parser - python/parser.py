#-*- coding: utf-8 -*-




#[('N', '2'),('+', '+'),('N', '3'),('-', '-'),('N', '4')]
# 2 + 3 - 4
# 2
# (+, 2, 3)
# (-, (+, 2, 3), 4)
def parse(tokens):
	if len(tokens) == 1:
		return int(tokens[0][1])

	try:
		if tokens[-2][0] == '*':
			return (tokens[-2][1], int(tokens[-1][1]), parse(tokens[:-2]))
	except:
		pass
	
	return (tokens[-2][1], parse(tokens[:-2]), int(tokens[-1][1]))


	#for i in range(1, len(tokens), 2):
	#	resultado = (tokens[i][0], resultado, int(tokens[i+1][1]))

	#return resultado