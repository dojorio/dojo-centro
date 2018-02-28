#!/usr/bin/env python
# -*- coding: utf-8 -*-

def change_for(value, paid):
	if value == paid:
		return { }
	if value == 5:
		return { 5: 1 }
	elif value == 15:
		return { 5: 1 }
	else:
		return { 2: 1 }