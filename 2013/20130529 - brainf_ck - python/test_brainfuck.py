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

    def test_exibe_0_1_2(self):
        programa = '.+.+.'
        entrada = ''
        saida = '\x00\x01\x02'
        self.assertEquals(saida, brainfuck(programa, entrada))

unittest.main()
