# -*- coding: utf-8 -*-
import unittest

from display7 import display

class TesteDisplay(unittest.TestCase):
    
    def teste_se_entrada_8_retorna_todos_segmentos_ativos(self):
        self.assertEquals(display(8), 
        """\
 ### 
#   #
#   #
#   #
 ### 
#   #
#   #
#   #
 ### """
        )

    def teste_se_entrada_0_retorna_zero_em_display_de_7_segmentos(self):
        self.assertEquals(display(0), 
        """\
 ### 
#   #
#   #
#   #
     
#   #
#   #
#   #
 ### """
        )
    
    def teste_se_entrada_1_retorna_1_em_display_de_7_segmentos(self):
        self.assertEquals(display(1), 
        """\
     
    #
    #
    #
     
    #
    #
    #
     """
        )
    def teste_se_entrada_3_retorna_3_em_display_de_7_segmentos(self):
        self.assertEquals(display(3),
        """\
 ### 
    #
    #
    #
 ### 
    #
    #
    #
 ### """
        )        
    def teste_se_entrada_9_retorna_9_em_display_de_7_segmentos(self):
        self.assertEquals(display(9),
        """\
 ### 
#   #
#   #
#   #
 ### 
    #
    #
    #
 ### """
        ) 
    def teste_se_entrada_88_retorna_88_em_display_de_7_segmentos(self):
        self.assertEquals(display(88),
        """\
 ###    ### 
#   #  #   #
#   #  #   #
#   #  #   #
 ###    ### 
#   #  #   #
#   #  #   #
#   #  #   #
 ###    ### """
        ) 
        
    def teste_se_entrada_831_retorna_831_em_display_de_7_segmentos(self):
        self.assertEquals(display(831),
        """\
 ###    ###        
#   #      #      #
#   #      #      #
#   #      #      #
 ###    ###        
#   #      #      #
#   #      #      #
#   #      #      #
 ###    ###        """
        )
    def teste_se_entrada_861_retorna_861_em_display_de_7_segmentos(self):
        self.assertEquals(display(861),
        """\
 ###    ###        
#   #  #          #
#   #  #          #
#   #  #          #
 ###    ###        
#   #  #   #      #
#   #  #   #      #
#   #  #   #      #
 ###    ###        """
        )   
unittest.main()