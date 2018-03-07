#!/usr/bin/env python
# -*- coding: utf-8 -*-

def change_for(value, paid):

	bills = [100,50,20,10,5,2,1,0.5,0.25,0.10, 0.05, 0.01]
	change = {}

	total_change = paid - value

	if value == paid:
		return { }
		
	else:
		for bill in bills:
			if (total_change >= bill):
				change[bill] = total_change // bill
				total_change = total_change % bill
		return change
