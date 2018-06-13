#!/usr/bin/env python
# -*- coding: utf-8 -*-

def my_party(expr):
	if '*' in expr:
		return '{}'
	if '-' in expr:
		first, second = expr.split('-')
		if first == second:
			return '{}' 

		clean_second = second.replace("{", "").replace("}", "")
		return first.replace(clean_second, "")

	result = expr
	if '+' in expr:
		result = expr.replace("}+{", "")
		result = "".join(set(result))

	return "{" + "".join(sorted(result.replace("{", "").replace("}",""))) + "}"