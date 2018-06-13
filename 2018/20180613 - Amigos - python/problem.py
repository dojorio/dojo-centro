#!/usr/bin/env python
# -*- coding: utf-8 -*-

def my_party(expr):
	if '+' in expr:
		result = expr.replace("}+{", "")
		unique(result.split()).join('')

	return expr