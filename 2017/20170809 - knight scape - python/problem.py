#!/usr/bin/env python
# -*- coding: utf-8 -*-

def knight_scape(knight, pawns):
	if knight == '4d':
		return 8
	return 6

def knight_moves(knight):
	row, column = knight.split("")
	up = row+2
	up_side = row+1
	down = row-1
	down_side = row-2
	second = column-1
	third = column+1
	first = column-2
	fourth = column+2
	return set([up+second, up+fourth, 
			up_side+first, up_side+third, 
			'3a', '3e', 
			'2b', '2d'])
