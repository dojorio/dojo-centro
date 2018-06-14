#!/usr/bin/env python
# -*- coding: utf-8 -*-

def my_party(expr):
	if '*' in expr:
		acc = list()
		first, second = expr.split('*')

		for ch in first.replace("{", "").replace("}", ""):
			if ch in second:
				acc.append(ch)

		return "{" + "".join(sorted(acc)) + "}"
		
	if '-' in expr:
		aux = ''
		for atual in expr.split('-'):
			if aux == '':
				aux = atual
			else:  
				clean_second = atual.replace("{", "").replace("}", "")				 
				aux = aux.replace(clean_second, "")
		return aux

	result = expr
	if '+' in expr:
		result = expr.replace("}+{", "")
		result = "".join(set(result))

	return "{" + "".join(sorted(result.replace("{", "").replace("}",""))) + "}"