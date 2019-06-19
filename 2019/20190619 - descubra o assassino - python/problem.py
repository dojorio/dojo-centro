#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Testemunha:
	def __init__(self, suspeito, arma, local):
		self.suspeito = suspeito
		self.arma = arma
		self.local = local

	def pergunta(self, suspeito, arma, local):
		return 1