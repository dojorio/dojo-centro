#!/usr/bin/env python
# -*- coding: utf-8 -*-

def gera_campo(campo):
	if campo == ['..']:
		return ['00']

	if campo == ['*']:
		return ['*']

	return ['0']
