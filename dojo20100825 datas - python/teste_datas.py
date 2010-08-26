#-*- coding: utf-8 -*-
import unittest
from datas import *

class Teste(unittest.TestCase):

    def test_dia_23_mes_06_ano_1987_eh_valido(self):
        self.assertEquals(valida_data("23/06/1987"), "válido")

    def test_dia_32_mes_06_ano_1987_eh_invalido(self):
        self.assertEquals(valida_data("32/06/1987"), "inválido")

    def test_dia_00_mes_06_ano_1987_invalido(self):
        self.assertEquals(valida_data("00/06/1987"),"inválido")

    def test_dia_1_mes_06_ano_1987_valido(self):
        self.assertEquals(valida_data("01/06/1987"),"válido")

    def test_dia_5_mes_05_ano_1987_valido(self):
        self.assertEquals(valida_data("05/05/1987"),"válido")

    def test_dia_1_mes_06_ano_2013_invalido(self):
        self.assertEquals(valida_data("01/06/2013"),"inválido")

class ValidadorDeAno(unittest.TestCase):
    def test_ano_1987_valido(self):
        self.assertEquals(valida_ano("1987"), True)

    def test_ano_0_invalido(self):
        self.assertEquals(valida_ano("0"), False)

    def test_ano_2013_invalido(self):
        self.assertEquals(valida_ano("2013"), False)






if __name__ == '__main__':
    unittest.main()

