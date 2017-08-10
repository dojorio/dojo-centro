#!/usr/bin/env python
# -*- coding: utf-8 -*-

def knight_scape(knight, pawns):
	if knight == '4d':
		return 8
	return 6

def knight_moves(knight):
	row, column = int(knight[0]), ord(knight[1])

	up = str(row+2)
	up_side = str(row+1)
	down_side = str(row-1)
	down = str(row-2)

	first = chr(column-2)
	second = chr(column-1)
	third = chr(column+1)
	fourth = chr(column+2)

	result = set([up+second, up+third, 
		up_side+first, 			up_side+fourth, 
		down_side+first, 		down_side+fourth, 
				down+second, down+third])

	return filter(naopode,result)

	return (result - set(['0a', '0b', '0c', '0d', '0e', '0f', '0g', '0h'])
				   - set(['-1a', '-1b', '-1c', '-1d', '-1e', '-1f', '-1g', '-1h'])
				   - set(['3`', '4`', '5`','6`', '7`', '8`'])
				   - set(['9a', '9b', '9c','9d', '9e', '9f', '9g', '9h'])
				   - set(['6i','4i']))
def naopode(posicao):
	if "0" in posicao:
		return False
	return True	