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
        self.assertEqual("pombo", quiz(voa=True))




if __name__ == "__main__":
    unittest.main()

