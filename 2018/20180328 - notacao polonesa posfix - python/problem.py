#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def transliterate(expression):
	is_statement = False
	statement = []
	polonese_statement = None

	for char in expression:
		if char in ['(', ')']:
			continue

		statement.append(char)
		if len(statement) == 3:
			polonese_statement = transliterate_without_parenthesis(statement)
			statement = [polonese_statement]

	return statement[0]

	# parte1 = expression[0]

	# if expression.startswith('(') and expression.endswith(')'):
	# 	expression = expression.strip('(').strip(')')
	# 	return transliterate_without_parenthesis(expression)

	# if expression.startswith('('):
	# 	if len(expression) == 5:
	# 		return 'ab+'
	# 	return 'ab+c+'

	# if expression.endswith(')'):
	# 	return 'ab' + expression[5] + '++'

	# if expression == "a+(b+c)+d": 
	# 	return "abc++d+"

	# return transliterate_without_parenthesis(expression)


def transliterate_without_parenthesis(expression):
 	
	parte1 = expression[0]

	for i in range(1, len(expression), 2):
		parte1 += expression[i + 1] + expression[i]

	return parte1
