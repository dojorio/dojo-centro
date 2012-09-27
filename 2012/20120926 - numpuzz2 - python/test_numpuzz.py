#coding: utf-8
import unittest
from numpuzz import numpuzz

class TestNumpuzz(unittest.TestCase):

    def test_vazio(self):
        tabuleiro = [
            0, 0, 0,
            0, 0, 0,
            0, 0, 0,
        ]
        self.assertEquals([], numpuzz(tabuleiro))

    def test_4(self):
        tabuleiro = [
            0, 1, 0,
            1, 1, 1,
            0, 1, 0,
        ]
        passos = [4]
        self.assertEquals(passos, numpuzz(tabuleiro))

    def test_4_4(self):
        tabuleiro = [
            0, 2, 0,
            2, 2, 2,
            0, 2, 0,
        ]
        
        passos = [4, 4]
        self.assertEquals(passos, numpuzz(tabuleiro))


    def test_3(self):
        tabuleiro = [
            1, 0, 0,
            1, 1, 0,
            1, 0, 0,
        ]
        passos = [3]
        self.assertEquals(passos, numpuzz(tabuleiro))
        
    def test_5(self):
        tabuleiro = [
            0, 0, 1,
            0, 1, 1,
            0, 0, 1,
        ]
        passos = [5]
        self.assertEquals(passos, numpuzz(tabuleiro))

    def test_1(self):
        tabuleiro = [
            1, 1, 1,
            0, 1, 0,
            0, 0, 0,
        ]
        passos = [1]
        self.assertEquals(passos, numpuzz(tabuleiro))

    def test_7(self):
        tabuleiro = [
            0, 0, 0,
            0, 1, 0,
            1, 1, 1,
        ]
        passos = [7]
        self.assertEquals(passos, numpuzz(tabuleiro))

    def test_7_7(self):
        tabuleiro = [
            0, 0, 0,
            0, 2, 0,
            2, 2, 2,
        ]
        passos = [7, 7]
        self.assertEquals(passos, numpuzz(tabuleiro))

    def test_0(self):
        tabuleiro = [
            1, 1, 0,
            1, 0, 0,
            0, 0, 0,
        ]
        passos = [0]
        self.assertEquals(passos, numpuzz(tabuleiro))

    def test_2(self):
        tabuleiro = [
            0, 1, 1,
            0, 0, 1,
            0, 0, 0,
        ]
        passos = [2]
        self.assertEquals(passos, numpuzz(tabuleiro))

    def test_8(self):
        tabuleiro = [
            0, 0, 0,
            0, 0, 1,
            0, 1, 1,
        ]
        passos = [8]
        self.assertEquals(passos, numpuzz(tabuleiro))
        
    def test_0_8(self):
        tabuleiro = [
            1, 1, 0,
            1, 0, 1,
            0, 1, 1,
        ]
        passos = [0, 8]
        self.assertEquals(passos, numpuzz(tabuleiro))
        
    def test_2_3(self):
        tabuleiro = [
            1, 1, 1,
            1, 1, 1,
            1, 0, 0,
        ]
        passos = [2, 3]
        self.assertEquals(passos, numpuzz(tabuleiro))
    
    def test_4_4_4(self):
        tabuleiro = [
            0, 3, 0,
            3, 3, 3,
            0, 3, 0,
        ]
        passos = [4, 4, 4]
        self.assertEquals(passos, numpuzz(tabuleiro))
        

unittest.main()
