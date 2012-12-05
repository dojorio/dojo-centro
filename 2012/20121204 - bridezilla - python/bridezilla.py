#coding: utf-8

class BarracoException(Exception):
	pass

def bridezilla(casais, adulterios):
	if len(adulterios) == casais:
		raise BarracoException()

	resultado = ['M%d' % n for n in range(casais)]

	for pessoa1, pessoa2 in adulterios:
		if 'H' in pessoa1 and 'H' in pessoa2:
			numero = int(pessoa2[1:])
			resultado[numero] = 'H%d' % numero

	return resultado
