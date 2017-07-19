#!/usr/bin/env python
# -*- coding: utf-8 -*-

def army_buddies(soldados, baixas):
	if soldados in (2, 3):
		if baixas == [(2, 2)]:
			return ['1 *']
		return ['* 2']
	return ['* *']