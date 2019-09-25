#!/usr/bin/env python
# -*- coding: utf-8 -*-

def valor_total(tamanho, eventos):
	for evento in eventos:
		if evento[2] == tamanho:
			return 10
		else:
			return 0
