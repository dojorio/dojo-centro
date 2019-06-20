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
		self.palpite_suspeito = 1
		self.palpite_arma = 1
		self.palpite_local = 1

	def tentativas(self, num_tentativas):
		while num_tentativas > 0:
			palpite = self.testemunha.pergunta(self.palpite_suspeito,
											   self.palpite_arma,
				 							   self.palpite_local)
			num_tentativas -= 1
			if palpite == 1:
				self.palpite_suspeito += 1
			if palpite == 2:
				self.palpite_arma += 1
			if palpite == 3:
				self.palpite_local += 1
			if palpite == 0:
				return [self.palpite_suspeito, self.palpite_arma, self.palpite_local]

		return palpite