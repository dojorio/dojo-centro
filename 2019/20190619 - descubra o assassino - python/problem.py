#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Testemunha:
	def __init__(self, suspeito, arma, local):
		self.suspeito = suspeito
		self.arma = arma
		self.local = local

	def pergunta(self, suspeito, arma, local):
		if suspeito != self.suspeito:
			return 1

		if arma == self.arma:
			if local == self.local:
				return 0
			return 3
		return 2

	def tentativas(self, num_tentativas):
		return [1,1,1]