#!/usr/bin/env python
# -*- coding: utf-8 -*-

def change_for(value, paid):

	bills = {100,50,20,10,5,2}

	if value == paid:
		return { }
	elif value == 5:
		return { 5: 1 }
	elif value == 15:
		return { 5: 1 }
	elif value == 20:
		return { 20: 1, 10: 1 }
	else:
		return { 2: 1 }