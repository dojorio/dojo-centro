# -*- coding: utf-8 -*-
import unittest

from musical_score import *

FA  = "  \n  \n  \no-\n  \n--\n  \n--\n  \n--\n  \n--\n  "
MI  = "  \n  \n  \n--\no \n--\n  \n--\n  \n--\n  \n--\n  "
RE  = "  \n  \n  \n--\n  \no-\n  \n--\n  \n--\n  \n--\n  "
DO  = "  \n  \n  \n--\n  \n--\no \n--\n  \n--\n  \n--\n  "
SI  = "  \n  \n  \n--\n  \n--\n  \no-\n  \n--\n  \n--\n  "
LA  = "  \n  \n  \n--\n  \n--\n  \n--\no \n--\n  \n--\n  "
SOL = "  \n  \n  \n--\n  \n--\n  \n--\n  \no-\n  \n--\n  "
FAm = "  \n  \n  \n--\n  \n--\n  \n--\n  \n--\no \n--\n  "
MIm = "  \n  \n  \n--\n  \n--\n  \n--\n  \n--\n  \no-\n  "

SI4  = "  \n  \n  \n--\n| \n|-\n| \no-\n  \n--\n  \n--\n  "

class Test(unittest.TestCase):
    
    def teste_traduz_F_de_cima_com_duracao_1(self):
        p = Partitura(FA)
        self.assertEqual('F', p.qual_eh_nota())
        
    def teste_traduz_E_de_cima_com_duracao_1(self):
        p = Partitura(MI)
        self.assertEqual('E', p.qual_eh_nota())    
        
    def teste_traduz_C_com_duracao_1(self):
        p = Partitura(DO)
        self.assertEqual('C', p.qual_eh_nota())
         
    def teste_traduz_B_com_duracao_1(self):
        p = Partitura(SI)
        self.assertEqual('B', p.qual_eh_nota())
        
    def teste_traduz_B_com_duracao_um_quarto(self):
        p = Partitura(SI4)
        self.assertEqual(4, p.qual_eh_duracao())
    
    def teste_traduz_B_com_duracao_1(self):
        p = Partitura(SI)
        self.assertEqual(1, p.qual_eh_duracao())

        
unittest.main()