#!/usr/bin/env python
# -*- coding: utf-8 -*-

def transliterate(expression):
	if len(expression) == 3:
		return expression[0] + expression[2] + expression[1]
	if len(expression) > 3:
		return expression[0] + expression[2] + expression[1] + expression[4] + expression[3]
	return expression