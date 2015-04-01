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

unittest.main()
