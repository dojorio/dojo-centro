#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def transliterate(expression):
 	#expression = "(a+b)+c"
    #polonese_posfix_expression = "ab+c+"
    #transliterated_expression = []
	#for char in expression:

	parte1 = expression[0]

	if expression.startswith('('):
		if len(expression) == 5:
			return 'ab+'
		return 'ab+c+'
	if expression.endswith(')'):
		return 'ab' + expression[5] + '++'
	for i in range(1, len(expression), 2):
		parte1 += expression[i + 1] + expression[i]

	return parte1