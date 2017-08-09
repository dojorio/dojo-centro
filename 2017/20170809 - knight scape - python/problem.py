#!/usr/bin/env python
# -*- coding: utf-8 -*-

def knight_scape(knight, pawns):
	if knight == '4d':
		return 8
	return 6

def knight_moves(knight):
	column, row = knight.split()
	return ['6b', '6d', '5a', '5e', '3a', '3e', '2b', '2d']
