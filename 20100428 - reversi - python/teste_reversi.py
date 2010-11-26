import unittest
from reversi import *

class TesteReversi(unittest.TestCase):
    
    def test_estado_inicial_na_vez_das_pretas(self):        
        estado_do_jogo = [[0,0,0,0],
                          [0,B,P,0],  
                          [0,P,B,0],  
                          [0,0,0,0]]  
        possiveis_jogadas = [[0,1,0,0],
                             [1,B,P,0],  
                             [0,P,B,1],  
                             [0,0,1,0]]  
        self.assertEquals(possiveis_jogadas, definir_possiveis_jogadas(P, estado_do_jogo))  
        
    def test_estado_inicial_na_vez_das_brancas(self):        
        estado_do_jogo = [[0,0,0,0],
                          [0,B,P,0],  
                          [0,P,B,0],  
                          [0,0,0,0]]  
        possiveis_jogadas = [[0,0,1,0],
                             [0,B,P,1],  
                             [1,P,B,0],  
                             [0,1,0,0]]  
        self.assertEquals(possiveis_jogadas, definir_possiveis_jogadas(B, estado_do_jogo))  

    def test_estado_inicial_com_uma_jogada_das_brancas(self):
        estado_do_jogo = [[0,0,B,0],
                          [0,B,B,0],  
                          [0,P,B,0],  
                          [0,0,0,0]]  
        possiveis_jogadas = [[0,1,B,1],
                             [0,B,B,0],  
                             [0,P,B,1],  
                             [0,0,0,0]]  
        self.assertEquals(possiveis_jogadas, definir_possiveis_jogadas(P, estado_do_jogo))  

        
if __name__ == '__main__':
    unittest.main()