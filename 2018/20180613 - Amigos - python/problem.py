#!/usr/bin/env python
# -*- coding: utf-8 -*-

def my_party(expr):
	if '-' in expr:
		dividido = expr.split('-')
		if dividido[0] == dividido[1]:
			return '{}' 
		return expr[:3]

	result = expr
	if '+' in expr:
		result = expr.replace("}+{", "")
		result = "".join(set(result))

	return "{" + "".join(sorted(result.replace("{", "").replace("}",""))) + "}"