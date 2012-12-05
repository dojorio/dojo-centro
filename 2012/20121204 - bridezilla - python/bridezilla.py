#coding: utf-8

class BarracoException(Exception):
	pass

def bridezilla(casais, adulterios):
	if len(adulterios) == casais:
		raise BarracoException()

	resultado = ['M%d' % n for n in range(casais)]

	for pessoa1, pessoa2 in adulterios:
		if parceiro(pessoa1) in resultado and parceiro(pessoa2) in resultado:
			numero = max(int(pessoa1[1:]), int(pessoa2[1:]))
			resultado[numero] = 'H%d' % numero

	return resultado

def parceiro(pessoa):
	numero = int(pessoa[1:])
	return '%s%d' % ('M' if pessoa[0] == 'H' else 'H', numero)