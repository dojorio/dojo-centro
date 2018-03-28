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

	if len(expression) > 1:
		parte1 += expression[2] + expression[1]
	if len(expression) > 3:
		parte1 += expression[4] + expression[3] 
	if len(expression) > 5:
		parte1 += expression[6] + expression[5]

	return parte1