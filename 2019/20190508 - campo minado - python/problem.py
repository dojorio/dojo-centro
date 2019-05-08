#!/usr/bin/env python
# -*- coding: utf-8 -*-

def gera_campo(campo):

	if campo == ['*']:
		return ['*']
	return[campo.replace('.', '0')]
	