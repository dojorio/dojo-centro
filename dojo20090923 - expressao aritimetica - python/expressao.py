# -*- coding: utf-8 -*-

def avaliador(expressao):
	try:
		return int(expressao)
	except:
		pass
	
	tokens = []
	operador = ""
	digito = "0"
	for char in expressao:
		if char.isdigit():
			digito += char
		else:
			tokens.append(operador + digito)
			operador = char
			digito = ""

	tokens.append(operador + digito)
		
	return sum(map(int, tokens)) 
