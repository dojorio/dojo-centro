#-*- coding: utf-8 -*-
import unittest
from brainfuck import brainfuck

class BrainfuckTestCase(unittest.TestCase):
    def test_exibe_zero(self):
        programa = '.'
        entrada = ''
        saida = '\x00'
        self.assertEquals(saida, brainfuck(programa, entrada))

    def test_exibe_zero_zero(self):
        programa = '..'
        entrada = ''
        saida = '\x00\x00'
        self.assertEquals(saida, brainfuck(programa, entrada))

    def test_exibe_um(self):
        programa = '+.'
        entrada = ''
        saida = '\x01'
        self.assertEquals(saida, brainfuck(programa, entrada))

    def test_exibe_dois(self):
        programa = '++.'
        entrada = ''
        saida = '\x02'
        self.assertEquals(saida, brainfuck(programa, entrada))


unittest.main()
