# -*- coding: utf-8 -*-
import unittest

from cipher import *
# expandir chave ate o tam. do texto

class TestCipher(unittest.TestCase):
        
    def test_ab(self):
        chave = 'B'
        texto = 'A'
        self.assertEqual('B',criptografa(texto,chave))
        
    def test_qualquer_texto_com_chave_B(self):
        chave = 'B'
        texto = 'HENRIQUE'
        self.assertEqual('IFOSJRWF',criptografa(texto,chave))
        
    def test_chave_igual_a_A_retorna_texto(self):
        chave = 'A'
        texto = 'WE'
        self.assertEqual(texto,criptografa(texto,chave))  
        texto = 'RODRIGO'
        self.assertEqual(texto,criptografa(texto,chave))  

    def test_qualquer_texto_com_chave_D(self):
        chave = 'D'
        texto = 'DOJORIO'
        self.assertEqual('GRMRULR',criptografa(texto,chave))

    def test_qualquer_texto_com_chave_Z(self):
        chave = 'Z'
        texto = 'ABC'
        self.assertEqual('ZAB',criptografa(texto,chave))
        
        
unittest.main()