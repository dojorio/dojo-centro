#!/usr/bin/env python
# -*- coding: utf-8 -*-

def transliterate(expression):
	if expression[0:1] == "a+":
		return "a" + expression[-1] + "+"

	return expression