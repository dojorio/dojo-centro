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

class Detetive:
	def __init__(self, testemunha):
		self.testemunha = testemunha

	def tentativas(self, num_tentativas):
		if self.suspeito != 1 and num_tentativas == 1:
			return 1

		return [self.suspeito, 1, 1]