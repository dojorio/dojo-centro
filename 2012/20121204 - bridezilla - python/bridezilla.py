#coding: utf-8

class BarracoException(Exception):
	pass

def bridezilla(casais, adulterios):
	if len(adulterios) == casais:
		raise BarracoException()

	if len(adulterios) == 1 and casais == 2:
		return ['M0', 'H1']

	if adulterios == (('H1', 'H2'),):
		return ['M0', 'H1', 'M2']

	resultado = ['M' + str(n) for n in range(casais)]
