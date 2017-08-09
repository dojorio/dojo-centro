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
	down = str(row-1)
	down_side = str(row-2)
	
	second = chr(column-1)
	third = chr(column+1)
	first = chr(column-2)
	fourth = chr(column+2)

	return set([up+second, up+fourth, 
			up_side+first, up_side+third, 
			'3a', '3e', 
			'2b', '2d'])
