#!/usr/bin/env python
# -*- coding: utf-8 -*-

def levenshtein(str1, str2):
	if str1 == str2:
		return 0

	n1 = len(str1)
	n2 = len(str2)

	substitutions = 0
	if n1 == n2:
		# replace
		for x in range(n1):
			if str1[x] != str2[x]:
				substitutions += 1

		return substitutions
		

	if len(str1) > len(str2):
		n_lowest = str2 + "X" * (len(n_highest) - len(n_lowest))
	else:
		n_lowest = str1 + "X" * (len(n_highest) - len(n_lowest))



	return  max(n1, n2) - min(n1, n2)
