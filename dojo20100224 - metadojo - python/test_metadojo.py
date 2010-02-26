# -*- coding: utf-8 -*-
import unittest

from metadojo import *

class TestDojo(unittest.TestCase):
	def test_nao_permite_menos_de_3_participantes(self):		
		pessoas = ['carina', 'raphael']
		dojo = Dojo()
		log_esperado = ['tem pouca gente', 'dojo acabou']
		
		self.assertEquals(log_esperado, dojo.run(pessoas))
		
	def test_permite_mais_de_3_participantes(self):		
		pessoas = ['carina', 'raphael', 'leandro']
		dojo = Dojo()
		log_esperado = ['ok']
		
		self.assertEquals(log_esperado, dojo.run(pessoas))
		
unittest.main()