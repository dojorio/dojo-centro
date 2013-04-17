#-*- coding: utf-8 -*-
import unittest
from aeroporto import aeroporto

class AeroportoTestCase(unittest.TestCase):
    def test_vazio(self):
        patio = ['*']
        self.assertEqual(0, aeroporto(patio))

    def test_com_um_lugar(self):
        patio = ['* ']
        self.assertEqual(1, aeroporto(patio))

    def test_com_um_lugar_na_vertical(self):
        patio = [' ',
                 '*']
        self.assertEqual(1, aeroporto(patio))

    def test_com_um_bloqueio(self):
        patio = ['*#']
        self.assertEqual(0, aeroporto(patio))

    def test_com_um_bloqueio_e_um_espaco_antes_do_bloqueio(self):
        patio = ['* #']
        self.assertEqual(1, aeroporto(patio))

    def test_com_um_bloqueio_e_um_espaco_depois_do_bloqueio(self):
        patio = ['*# ']
        self.assertEqual(0, aeroporto(patio))


unittest.main()
