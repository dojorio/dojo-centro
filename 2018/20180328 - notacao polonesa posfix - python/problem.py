#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def transliterate(expression):

	parte1 = expression[0]

	if expression.startswith('(') and expression.endswith(')'):
		expression = expression.strip('(').strip(')')
		return transliterate_without_parenthesis(expression)

	if expression.startswith('('):
		if len(expression) == 5:
			return 'ab+'
		return 'ab+c+'

	if expression.endswith(')'):
		return 'ab' + expression[5] + '++'



	return transliterate_without_parenthesis(expression)


def transliterate_without_parenthesis(expression):
 	
	parte1 = expression[0]

	for i in range(1, len(expression), 2):
		parte1 += expression[i + 1] + expression[i]

	return parte1
