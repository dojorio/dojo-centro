import unittest
from star import star

class TestStar(unittest.TestCase):
    
    def test_1_linha_area1(self):
        triangulo = ['-']
        self.assertEqual(star(triangulo), 1)
    
    def test_1_linha_area0(self):
        triangulo = ['#']
        self.assertEqual(star(triangulo), 0)

    def test_2_linhas_area4(self):
        triangulo = ['---',
                      '-']
        self.assertEqual(star(triangulo), 4)

    def test_2_linhas_area1(self):
        triangulo = ['-#-',
                      '-']
        self.assertEqual(star(triangulo), 1)


    def test_3_linhas_area4(self):
        triangulo = ['-----',
                      '-#-',
                       '-']
        self.assertEqual(star(triangulo), 4)

    def test_3_linhas_area9(self):
        triangulo = ['-----',
                      '---',
                       '-']
        self.assertEqual(star(triangulo), 9)

    def test_4_linhas_area9(self):
        triangulo = ['-------',
                      '-----',
                       '-#-',
                        '-']
        self.assertEqual(star(triangulo), 9) 

    def test_2_linhas_area1_reloaded(self):
        triangulo = ['##-',
                      '-']
        self.assertEqual(star(triangulo), 1) 

    def test_2_linhas_area1_no_meio(self):
        triangulo = ['#-#',
                      '#']
        self.assertEqual(star(triangulo), 1) 


unittest.main()
