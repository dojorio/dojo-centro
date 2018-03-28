#!/usr/bin/env python
# -*- coding: utf-8 -*-

def transliterate(expression):
	if expression[0] + expression[1] == "a+":
		return expression[0] + expression[1] + "+" 

	return expression