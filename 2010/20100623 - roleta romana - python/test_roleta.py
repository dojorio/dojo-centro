# -*- coding: utf-8 -*-
import unittest
from roleta import *


class TesteRoleta(unittest.TestCase):

    def test_1_pessoas_1_passo_pessoa_1_sobrevive(self):
        sobrevivente = roleta(numero_de_pessoas = 1, passo = 1)
        self.assertEqual( sobrevivente, 1)

    def test_1_pessoas_2_passo_pessoa_1_sobrevive(self):
        sobrevivente = roleta(numero_de_pessoas = 1, passo = 2)
        self.assertEqual( sobrevivente, 1)

    def test_1_pessoas_3_passo_pessoa_1_sobrevive(self):
       sobrevivente = roleta(numero_de_pessoas = 1, passo = 3)
       self.assertEqual( sobrevivente, 1)

    def test_2_pessoas_1_passo_pessoa_2_sobrevive(self):
        sobrevivente = roleta(numero_de_pessoas = 2, passo = 1)
        self.assertEqual( sobrevivente, 2)

    def test_2_pessoas_2_passos_pessoa_1_sobrevive(self):
        sobrevivente = roleta(numero_de_pessoas = 2, passo = 2)
        self.assertEqual( sobrevivente, 1)

    def test_2_pessoas_3_passos_pessoa_2_sobrevive(self):
        sobrevivente = roleta(numero_de_pessoas = 2, passo = 3)
        self.assertEqual( sobrevivente, 2)

    def test_2_pessoas_4_passos_pessoa_1_sobrevive(self):
        sobrevivente = roleta(numero_de_pessoas = 2, passo = 4)
        self.assertEqual( sobrevivente, 1)



    def test_2_pessoas_2_passos_pessoa_1_sobrevive(self):
        sobrevivente = roleta(numero_de_pessoas = 2, passo = 2)
        self.assertEqual( sobrevivente, 1)

    def test_2_pessoas_3_passos_pessoa_2_sobrevive(self):
        sobrevivente = roleta(numero_de_pessoas=2, passo=3)
        self.assertEqual(sobrevivente, 2)


    def test_3_pessoas_3_passos_pessoa_2_sobrevive(self):
        sobrevivente = roleta(numero_de_pessoas = 3, passo = 3)
        self.assertEqual(sobrevivente, 2)

    def test_3_pessoas_2_passos_pessoa_3_sobrevive(self):
        sobrevivente = roleta(numero_de_pessoas = 3, passo = 2)
        self.assertEqual(sobrevivente, 3)

    def test_4_pessoas_3_passos_pessoa_4_sobrevive(self):
        sobrevivente = roleta(numero_de_pessoas = 4, passo = 3)
        self.assertEqual(sobrevivente, 4)


unittest.main()

