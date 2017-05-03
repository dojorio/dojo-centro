#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from animal_quiz import *


class TestSolution(unittest.TestCase):
    def test_(self):
        quiz = Quiz()
        self.assertEqual("cachorro", quiz.advinha())

class TestProblem(unittest.TestCase):
    def test_cachorro(self):
        self.assertEqual("cachorro", quiz())

    def test_gato(self):
        self.assertEqual("gato", quiz(mia=True))

    def test_pombo(self):
        self.assertEqual("pombo", quiz(voa=True, pena=True))

    def test_morcego(self):
        self.assertEqual("morcego", quiz(voa=True, pena=False))

    def test_macaco(self):
        self.assertEqual("macaco", quiz(come_banana=True))

    def test_galinha(self):
        self.assertEqual("galinha", quiz(pena=True))

    def test_pato(self):
        self.assertEqual("pato", quiz(pena=True, nada=True))

    def test_hipopotamo(self):
        self.assertEqual("hipopotamo", quiz(nada=True, couro=True))
    
    def test_cavalo(self):
        self.assertEqual("cavalo", quiz(couro=True))





if __name__ == "__main__":
    unittest.main()

