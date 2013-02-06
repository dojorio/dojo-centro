#-*- coding: utf-8 -*-
def parse(tokens):
	result = []
	if len(tokens) == 3:
		return (tokens[1][0], 2, 2)
	return int(tokens[0][1])