# -*- coding: utf-8 -*-
import unittest
from wordwrap import wordwrap, NotWrappableError

class TestWordWrap(unittest.TestCase):
	def test_frase_vazia_nao_quebra_linha(self):
		self.assertEqual(wordwrap("", 80), "")
	
	def test_uma_palavra_menor_que_tamanho_linha(self):
		self.assertEqual(wordwrap("abobora", 80), "abobora")
		
	def test_uma_palavra_maior_que_tamanho_linha(self):
		self.assertEqual(wordwrap("abobora", 5), "abobo\nra")
	
	def test_uma_palavra_muito_maior_que_tamanho_linha(self):
		self.assertEqual(wordwrap("abobora", 2), "ab\nob\nor\na")
		
	def test_uma_frase_que_quebra_antes_do_espaco(self):		
		self.assertEqual(wordwrap("abobora legal", 7), "abobora\nlegal")
		
	def test_uma_frase_que_quebra_exatamente_no_espaco(self):
		self.assertEqual(wordwrap("abobora legal", 8), "abobora\nlegal")
	
	def test_uma_frase_que_quebra_apos_do_espaco(self):	
		self.assertEqual(wordwrap("abobora legal", 9), "abobora\nlegal")
		self.assertEqual(wordwrap("limao legal", 9), "limao\nlegal")
		self.assertEqual(wordwrap("limao legal", 10), "limao\nlegal")
	
	def test_uma_frase_que_comeca_com_espaco(self):
		self.assertEqual(wordwrap(" abobora legal", 8), " abobora\nlegal")
	
unittest.main()



