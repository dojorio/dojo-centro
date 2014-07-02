import unittest
from oitorainhas import oitorainhas

class OitoRainhas(unittest.TestCase):
    def test_tabuleiro_sem_nenhuma_rainha(self):
        tabuleiro = [ 
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],  
        ]
        self.assertEqual(oitorainhas(tabuleiro), False)

def test_tabuleiro_com_uma_rainha(self):
        tabuleiro = [ 
            [1,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],  
        ]
        self.assertEqual(oitorainhas(tabuleiro), False)


unittest.main() 