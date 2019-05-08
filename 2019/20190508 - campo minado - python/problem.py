#!/usr/bin/env python
# -*- coding: utf-8 -*-

def gera_campo(campo):
	if campo == ['*']:
		return ['*']

	if campo == ['*.']:
		return ['*1']

	if campo == ['.*']:
		return ['1*']

	return [campo[0].replace('.', '0')]
	