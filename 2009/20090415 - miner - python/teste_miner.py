import unittest

import miner
from textwrap import dedent

class TesteMiner(unittest.TestCase):
    def teste_square_matrix(self):
        col = 3
        row = 3
        matrix = miner.start_matrix(col, row)
        cells = 0
        for i in matrix:
            for j in i:
                cells += 1
                
        self.assertEqual(cells, col * row)
    
    def teste_col_only_matrix(self):
        col = 7
        row = 1
        matrix = miner.start_matrix(col, row)
        cells = 0
        for i in matrix:
            cells += 1
                
        self.assertEqual(cells, col)

    
    def teste_row_only_matrix(self):
        col = 1
        row = 8
        matrix = miner.start_matrix(col, row)
        cells = 0
        for i in matrix[0]:
            cells += 1
                
        self.assertEqual(cells, row)
        
    def teste_empty_matrix(self):
        col = 9
        row = 8
        matrix = miner.start_matrix(col, row)
        soma = 0
        for linha in matrix:
            for celula in linha:
                soma += celula
                
        self.assertEqual(soma, 0)
        
    def teste_verificar_bomba(self):
        col = 12
        row = 8
        matrix = miner.start_matrix(col, row)
        miner.coloca_bomba(matrix, 3,7)
        
        self.assertEqual(matrix[3][7], -1) 
        
    def teste_verificar_vizinhanca(self):
        col = 3
        row = 3
        matrix = miner.start_matrix(col, row)
        matrix = miner.coloca_bomba(matrix, 1,1)
        matrix = miner.define_valor(matrix, 0,0)
        
        
        self.assertEqual(matrix[0][0], 1)
    
        
        
unittest.main()        
