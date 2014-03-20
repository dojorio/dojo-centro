import unittest
from erdos import classificaErdos

class TestErdos(unittest.TestCase):
    def test_so_erdos_escreveu(self):
        livros = [('Erdos',)]
        self.assertEqual(classificaErdos('Erdos', livros), 0)

    def test_mais_1_escreveu(self):
        livros = [('Erdos','Carlos')]
        self.assertEqual(classificaErdos('Carlos', livros), 1)

    def test_mais_2_escreveram_com_erdos_2(self):
        livros = [('Erdos','Carlos'), ('Carlos', 'Flávio')]
        self.assertEqual(classificaErdos('Flávio', livros), 2)
    
    def test_4(self):
        livros = [('Erdos','Flávio')]
        self.assertEqual(classificaErdos('Flávio', livros), 1)

    def test_5(self):
        livros = [('Erdos','Flávio'), ('Carlos', 'Flávio')]
        self.assertEqual(classificaErdos('Flávio', livros), 1)

    def test_6(self):
        livros = [('Erdos','Flávio'), ('Carlos', 'Flávio'), ('Erdos',)]
        self.assertEqual(classificaErdos('Carlos', livros), 2)

    def test_7(self):
        livros = [('Erdos','Flávio'), ('Otávio', 'Flávio'), ('Carlos','Otávio')]
        self.assertEqual(classificaErdos('Carlos', livros), 3)

unittest.main()
