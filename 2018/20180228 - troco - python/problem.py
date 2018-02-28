#!/usr/bin/env python
# -*- coding: utf-8 -*-

def change_for(value, paid):

	bills = [100,50,20,10,5,2]

	troco_total = paid - value

	if value == paid:
		return { }
	elif troco_total in bills:
		return { troco_total: 1 } 
	elif troco_total == 4:
		for bill in bills:
			quantidade = troco_total / bill
		return { bill: quantidade}
	elif value == 20:
	   return { 20: 1, 10: 1 }
	else:
		return { 2: 1 }