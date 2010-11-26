# -*- coding: utf-8 -*-
import unittest
from automato import *

transicoes_de_estado = [(0,'9',1),(1,'+',0)]
estados_finais = [1]

class TesteParser(unittest.TestCase):
    
    def test_um_operando(self):
        expressao = '9'
        eh_valido = parser(transicoes_de_estado, estados_finais, expressao)
        self.assertTrue(eh_valido)


    def test_um_operador(self):
        expressao = '+'
        eh_valido = parser(transicoes_de_estado, estados_finais, expressao)
        self.assertFalse(eh_valido)

    def test_um_operando_e_um_operador(self):
        expressao = '9+'
        eh_valido = parser(transicoes_de_estado, estados_finais, expressao)
        self.assertFalse(eh_valido)

    def test_operando_operador_operando(self):
        expressao = '9+9'
        eh_valido = parser(transicoes_de_estado, estados_finais, expressao)
        self.assertTrue(eh_valido)

    def test_operando_operador_operador_operando(self):
        expressao = '9++9'
        eh_valido = parser(transicoes_de_estado, estados_finais, expressao)
        self.assertFalse(eh_valido)

    def test_operando_operador_operando_operador(self):
        expressao = '9+9+'
        eh_valido = parser(transicoes_de_estado, estados_finais, expressao)
        self.assertFalse(eh_valido)

    def test_operando_operador_operando_operando(self):
        expressao = '9+99'
        eh_valido = parser(transicoes_de_estado, estados_finais, expressao)
        self.assertFalse(eh_valido)

    def test_uma_transicao_estado_zero(self):
        estado_atual=0
        transicao=(0,'9',1)
        transicao_final = executa_transicao(estado_atual,transicao)
        self.assertEquals(1,transicao_final)

    def test_uma_transicao_estado_(self):
        estado_atual=1
        transicao=(1,'+',0)
        transicao_final = executa_transicao(estado_atual,transicao)
        self.assertEquals(0,transicao_final)

unittest.main()
