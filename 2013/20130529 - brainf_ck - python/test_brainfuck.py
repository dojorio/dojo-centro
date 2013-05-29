#-*- coding: utf-8 -*-
import unittest
from brainfuck import brainfuck

class BrainfuckTestCase(unittest.TestCase):
    def test_exibe_0(self):
        programa = '.'
        entrada = ''
        saida = '\x00'
        self.assertEquals(saida, brainfuck(programa, entrada))

    def test_exibe_0_0(self):
        programa = '..'
        entrada = ''
        saida = '\x00\x00'
        self.assertEquals(saida, brainfuck(programa, entrada))

    def test_exibe_1(self):
        programa = '+.'
        entrada = ''
        saida = '\x01'
        self.assertEquals(saida, brainfuck(programa, entrada))

    def test_exibe_2(self):
        programa = '++.'
        entrada = ''
        saida = '\x02'
        self.assertEquals(saida, brainfuck(programa, entrada))

    def test_exibe_255(self):
        programa = '-.'
        entrada = ''
        saida = '\xFF'
        self.assertEquals(saida, brainfuck(programa, entrada))


    def test_incrementa_256_vezes_e_exibe_0(self):
        programa = '+' * 256 + '.'
        entrada = ''
        saida = '\x00'
        self.assertEquals(saida, brainfuck(programa, entrada))

    def test_exibe_0_1(self):
        programa = '.+.'
        entrada = ''
        saida = '\x00\x01'
        self.assertEquals(saida, brainfuck(programa, entrada))

    def test_exibe_0_1_2(self):
        programa = '.+.+.'
        entrada = ''
        saida = '\x00\x01\x02'
        self.assertEquals(saida, brainfuck(programa, entrada))

    def test_le_A_e_exibe_A(self):
        programa = ',.'
        entrada = 'A'
        saida = '\x41'
        self.assertEquals(saida, brainfuck(programa, entrada))

    def test_le_AB_e_exibe_B(self):
        programa = ',,.'
        entrada = 'AB'
        saida = '\x42'
        self.assertEquals(saida, brainfuck(programa, entrada))
unittest.main()
