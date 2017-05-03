#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from animal_quiz import *


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




if __name__ == "__main__":
    unittest.main()

