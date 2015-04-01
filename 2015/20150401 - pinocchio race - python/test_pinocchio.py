import unittest
from pinocchio import corrida
class TestPinocchio(unittest.TestCase):
    def test_empate(self):
        pinoquio1, pinoquio2 = (1,.1), (1, .1)
        pista = 5.1
        self.assertEqual(corrida(pinoquio1, pinoquio2, pista), 'empate')

    def pinocchio1_vence(self):
        

unittest.main()
