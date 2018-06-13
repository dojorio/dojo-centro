#!/usr/bin/env python
# -*- coding: utf-8 -*-

def my_party(expr):
	if '+' in expr:
		result = expr.replace("}+{", "")
		result = "".join({n for n in result})

	return result