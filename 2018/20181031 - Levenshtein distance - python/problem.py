#!/usr/bin/env python
# -*- coding: utf-8 -*-

def levenshtein(str1, str2):
	if str1 == str2:
		return 0

	n1 = len(str1)
	n2 = len(str2)
	n_highest = max(str1, str2)
	n_lowest = min(str1, str2)
	if lenn_highest !=

	substitutions = 0
	if n1 == n2:
		# replace
		for x in range(n1):
			if str1[x] != str2[x]:
				substitutions += 1

		return substitutions

	return  max(n1, n2) - min(n1, n2)
