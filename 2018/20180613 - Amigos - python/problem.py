#!/usr/bin/env python
# -*- coding: utf-8 -*-

def my_party(expr):
	if '-' in expr:
		return expr[:expr.index('}')+1]

	result = expr
	if '+' in expr:
		result = expr.replace("}+{", "")
		result = "".join(set(result))

	return "{" + "".join(sorted(result.replace("{", "").replace("}",""))) + "}"