#coding: utf-8
import unittest
from decisao import indefinidos

class TestDecisao(unittest.TestCase):
    def test_uma_condicao_nenhum_indefinido(self):
        tabela = [
            ("*", "A")
        ]

        self.assertEqual(set([]), indefinidos(tabela))

    def test_uma_condicao_um_indefinido(self):
        tabela = [
            ("0", "A")
        ]

        self.assertEqual(set(["1"]), indefinidos(tabela))

    def test_uma_condicao_outro_indefinido(self):
        tabela = [
            ("1", "A"),
        ]

        self.assertEqual(set(["0"]), indefinidos(tabela))

    def test_uma_condicao_duas_regras(self):
        tabela = [
            ("1", "A"),
            ("0", "B"),
        ]

        self.assertEqual(set([]), indefinidos(tabela))

    def test_uma_condicao_duas_regras_redundantes(self):
        tabela = [
            ("1", "A"),
            ("1", "A"),
        ]

        self.assertEqual(set(["0"]), indefinidos(tabela))

    def test_uma_condicao_duas_regras_redundantes_outro(self):
        tabela = [
            ("1", "A"),
            ("*", "A"),
        ]

        self.assertEqual(set([]), indefinidos(tabela))

    def test_duas_condicoes_nenhum_indefinido(self):
        tabela = [
            ("**", "A")
        ]

        self.assertEqual(set([]), indefinidos(tabela))

    def test_duas_condicoes_uma_regra_indefinida(self):
        tabela = [
            ("01", "A"),
            ("00", "A"),
            ("10", "A")
        ]

        self.assertEqual(set(["11"]), indefinidos(tabela))

    def test_duas_condicoes_duas_regras_indefinidas(self):
        tabela = [
            ("01", "A"),
            ("10", "A")
        ]

        self.assertEqual(set(["11", "00"]), indefinidos(tabela))

    def test_duas_condicoes_duas_regras_indefinidas_com_solzinho(self):
        tabela = [
            ("0*", "A")
        ]

        self.assertEqual(set(["11", "10"]), indefinidos(tabela))

    def test_duas_condicoes_duas_regras_indefinidas_e_solzinho(self):
        tabela = [
            ("1*", "A")
        ]

        self.assertEqual(set(["00", "01"]), indefinidos(tabela))

    

unittest.main()