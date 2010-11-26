# -*- coding: utf-8 -*-
import unittest
from poker import poker

class TestesPoker(unittest.TestCase):

    def test_as_ganha_de_k(self):
        
        mao1 = "14C 2P 3O 4E 5O"
        
        mao2 = "13O 2E 3P 4O 5E"
        
        self.assertEqual(
            "Mao 1 (%s) ganha da Mao 2 (%s)" % (mao1, mao2), 
            poker(mao1, mao2)
        )
    def test_k_ganha_de_q(self):
        
        mao1 = "12C 2P 3O 4E 5O"
        
        mao2 = "13O 2E 3P 4O 5E"
        
        self.assertEqual(
            "Mao 2 (%s) ganha da Mao 1 (%s)" % (mao2, mao1), 
            poker(mao1, mao2)
        )
    def test_par_de_k_ganha_de_k(self):
        
        mao1 = "13C 13P 3O 4E 5O"
        mao2 = "13O 2E 3P 4O 5E"
        
        self.assertEqual(
            "Mao 1 (%s) ganha da Mao 2 (%s)" % (mao1, mao2), 
            poker(mao1, mao2)
        )
    def test_par_de_8_ganha_de_as(self):
        
        mao1 = "8C 8P 3O 4E 5O"
        mao2 = "14O 2E 3P 4O 5E"
        
        self.assertEqual(
            "Mao 1 (%s) ganha da Mao 2 (%s)" % (mao1, mao2), 
            poker(mao1, mao2)
        )

    def test_trinca_de_8_ganha_de_as(self):
        
        mao1 = "8C 8P 8O 4E 5O"
        mao2 = "14O 2E 3P 4O 5E"
        
        self.assertEqual(
            "Mao 1 (%s) ganha da Mao 2 (%s)" % (mao1, mao2), 
            poker(mao1, mao2)
        )
        
    def test_trinca_de_8_ganha_de_par_de_as(self):
        
        mao1 = "8C 8P 8O 4E 5O"
        mao2 = "14O 14E 3P 4O 5E"
        
        self.assertEqual(
            "Mao 1 (%s) ganha da Mao 2 (%s)" % (mao1, mao2), 
            poker(mao1, mao2)
        )
        
    def test_trinca_de_2_ganha_de_par_de_8(self):
        
        mao1 = "2C 2P 2O 4E 5O"
        mao2 = "8O 8E 3P 4O 5E"
        
        self.assertEqual(
            "Mao 1 (%s) ganha da Mao 2 (%s)" % (mao1, mao2), 
            poker(mao1, mao2)
        )

unittest.main()