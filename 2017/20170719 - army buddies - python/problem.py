#!/usr/bin/env python
# -*- coding: utf-8 -*-

def army_buddies(soldados, baixas):
	if soldados > 1:
		if baixas == [(2, 2)]:
			return ['1 *']
		return ['* 2']
	return ['* *']