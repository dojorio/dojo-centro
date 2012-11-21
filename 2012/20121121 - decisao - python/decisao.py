#coding: utf-8
import re

def indefinidos(tabela):
	qtd_condicoes = len(tabela[0][0])

	if qtd_condicoes == 1:
		gabarito = set(["0", "1"])
	else:
		gabarito = set(["00", "01", "10", "11"])

	# gabarito = gera_gabarito(qtd_condicoes)

	for regra in tabela:
		gabarito = remove_gabarito(gabarito, regra[0])
			
	return gabarito

def remove_gabarito(gabarito, condicoes):
	regexp = condicoes.replace('*', '.')

	return set(x for x in gabarito if not re.match(regexp, x))

# Não funciona :(
def gera_gabarito(n):
	gabarito = []

	for i in range(2 ** n):
		gabarito.append("{0:#b}".format(i))

	return set(gabarito)
