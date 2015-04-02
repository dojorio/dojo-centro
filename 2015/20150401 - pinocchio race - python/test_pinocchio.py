import unittest
from pinocchio import corrida

class TestPinocchio(unittest.TestCase):
    def test_empate(self):
        pinoquio1 = pinoquio2 = (1, 0.1)
        pista = 5.1
        resultado = corrida(pinoquio1, pinoquio2, pista)
        self.assertEqual(resultado, 'empate')

    def test_pinocchio1_vence(self):
        pinoquio1, pinoquio2 = (1, 0.2), (1, 0.1)
        pista = 5.3
        resultado = corrida(pinoquio1, pinoquio2, pista)
        self.assertEqual(resultado, 'pinoquio1')

    def test_pinocchio2_vence(self):
        pinoquio1, pinoquio2 = (1, 0.1), (1, 0.2)
        pista = 5.3
        resultado = corrida(pinoquio1, pinoquio2, pista)
        self.assertEqual(resultado, 'pinoquio2')

    def test_pinocchio1_narigudo_vence(self):
        pinoquio1, pinoquio2 = (1, 0.3), (1, 0.1)
        pista = 5.3
        resultado = corrida(pinoquio1, pinoquio2, pista)
        self.assertEqual(resultado, 'pinoquio1')

    def test_empate_com_nariz_iguais(self):
        pinoquio1, pinoquio2 = (1, 0.3), (1, 0.3)
        pista = 5.3
        resultado = corrida(pinoquio1, pinoquio2, pista)
        self.assertEqual(resultado, 'empate')

    def test_empate_pista_curta(self):
        pinoquio1, pinoquio2 = (1, 0.3), (1, 0.3)
        pista = 1.3
        resultado = corrida(pinoquio1, pinoquio2, pista)
        self.assertEqual(resultado, 'empate')

    def test_pinoquio1_vence_pista_curta(self):
        pinoquio1, pinoquio2 = (1, 0.5), (1, 0.1)
        pista = 5
        resultado = corrida(pinoquio1, pinoquio2, pista)
        self.assertEqual(resultado, 'pinoquio1')

    def test_pinoquio2_vence_sendo_mais_rapido(self):
        pinoquio1, pinoquio2 = (2, 0.1), (1, 0.1)
        pista = 5
        resultado = corrida(pinoquio1, pinoquio2, pista)
        self.assertEqual(resultado, 'pinoquio2')

    def test_pinoquio2_vence_sendo_mais_rapido_ainda(self):
        pinoquio1, pinoquio2 = (3, 0.1), (1, 0.1)
        pista = 5
        resultado = corrida(pinoquio1, pinoquio2, pista)
        self.assertEqual(resultado, 'pinoquio2')

    def test_pinoquio1_vence_sendo_mais_rapido(self):
        pinoquio1, pinoquio2 = (1, 0.1), (2, 0.1)
        pista = 5
        resultado = corrida(pinoquio1, pinoquio2, pista)
        self.assertEqual(resultado, 'pinoquio1')

    def test_pinoquio1_grande_vence_pelo_nariz_maior(self):
        pinoquio1, pinoquio2 = (4, 4), (2, 0.5)
        pista = 5
        resultado = corrida(pinoquio1, pinoquio2, pista)
        self.assertEqual(resultado, 'pinoquio1')

    def test_pequeno_vence_narigudo_na_pista_grande(self):
        pinoquio1, pinoquio2 = (4, 4), (2, 0.5)
        pista = 8
        resultado = corrida(pinoquio1, pinoquio2, pista)
        self.assertEqual(resultado, 'pinoquio2')

unittest.main()
