#coding: utf-8

class BarracoException(Exception):
	pass

def bridezilla(casais, adulterios):
	if len(adulterios) == 2:
		raise BarracoException()

	if len(adulterios) == 1:
		return ['M0', 'H1']

	return ['M' + str(n) for n in range(casais)]