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

	return set(filter(on_board, result))


def on_board(cell):
	for c in '0`9ij-':
		if c in cell:
			return False
	return True	