# -*- coding: utf-8 -*-
class TemPoucaGente(Exception):	pass
	
class Dojo:

	def __init__(self): pass
	
	def run(self, pessoas):
		if len(pessoas) < 3:
			return ['tem pouca gente', 'dojo acabou']
		return ['ok']
