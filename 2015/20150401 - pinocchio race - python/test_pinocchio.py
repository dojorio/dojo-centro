import unittest

class TestPinocchio(unittest.TestCase):
    def test_pass(self):
        pinoquio1, pinoquio2 = (1,.1), (1, .1)
        pista = 1.1
        self.assertEqual(corrida(pinoquio1, pinoquio2, pista), 'empate')
        

unittest.main()
