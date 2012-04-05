import unittest
from maze import solve, find_begin

class TestMaze(unittest.TestCase):
    def test_andar_pro_lado(self):
        maze = ('.x',)
        self.assertEqual(1, solve(maze))

    def test_andar_dois_passos_pro_lado(self):
        maze = ('. x',)
        self.assertEqual(2, solve(maze))

    def test_andar_dois_passos_em_duas_linhas(self):
        maze = ('. ',
                ' x')
        self.assertEqual(2, solve(maze))

    def test_andar_pro_lado_mas_tem_duas_linhas(self):
        maze = ('.x ',
                '   ')
        self.assertEqual(1, solve(maze))

    def test_andar_tres_passos_em_duas_linhas(self):
        maze = ('.  ',
                '  x')
        self.assertEqual(3, solve(maze))

    def test_andar_tres_passos_em_duas_linhas_com_inicio_e_fim_invertidos(self):
        maze = ('x  ',
                '  .')
        self.assertEqual(3, solve(maze))


    def test_andar_quatro_passos_em_duas_linhas(self):
        maze = ('.#x',
                '   ')
        self.assertEqual(4, solve(maze))
        
    def test_andar_seis_passos_em_tres_linhas(self):
        maze = ('.#x',
                ' # ',
                '   ')
        self.assertEqual(6, solve(maze))

    def test_andar_cinco_passos_em_tres_linhas(self):
        maze = ('.# ',
                ' #x',
                '   ')
        self.assertEqual(5, solve(maze))
        
    def test_andar_quatro_passos_em_tres_linhas(self):
        maze = ('.#x',
                '   ',
                ' # ')
        self.assertEqual(4, solve(maze))
        
    def test_andar_quatro_passos_em_tres_linhas_invertido(self):
        maze = ('x#.',
                '   ',
                ' # ')
        self.assertEqual(4, solve(maze))
    
    def test_andar_10_passos_em_cinco_colunas_sendo_duas_de_obstaculos(self):
        maze = ('.#   ',
                ' # # ',
                '   #x')
        self.assertEqual(10, solve(maze))
        
    def test_ir_para_a_direita_vai_dar_problema(self):
        maze = ('      ',
                '  . x ',
                '      ',
                '      ' )
        self.assertEqual(2, solve(maze))
        
    

class TestSearch(unittest.TestCase):
    def test_encontra_inicio_do_labirinto(self):
        maze = ('. ',)
        self.assertEqual((0,0), find_begin(maze))

    def test_encontra_inicio_do_labirinto_na_segunda_linha(self):
        maze = ('  ', 
                ' .')
        self.assertEqual((1,1), find_begin(maze))

        
unittest.main()
