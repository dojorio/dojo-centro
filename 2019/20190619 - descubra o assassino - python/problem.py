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
		if arma != self.arma:
			return 2
		if local != self.local:
			return 3
		return 0
		

class Detetive:
	def __init__(self, testemunha):
		self.testemunha = testemunha
		self.palpite = [1,1,1]

	def tentativas(self, num_tentativas):
		while num_tentativas > 0:
			palpite = self.testemunha.pergunta(self.palpite[0],
											   self.palpite[1],
				 							   self.palpite[2])
			num_tentativas -= 1
			if palpite > 0:
				self.palpite[palpite-1]  += 1
			else:
				return self.palpite
		return palpite