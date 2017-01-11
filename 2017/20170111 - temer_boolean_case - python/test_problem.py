#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestTemerUmCaracter(unittest.TestCase):
    def test_vai_ter_impeachment(self):
        self.assertTrue(impeachment("s"))

    def test_nao_vai_ter_golpe(self):
        self.assertFalse(impeachment("n"))

    def test_golpista_deu_golpe(self):
    	self.assertTrue(impeachment("S"))

    def test_dois_golpistas_deu_golpe(self):
    	self.assertTrue(impeachment("ss"))


if __name__ == "__main__":
    unittest.main()

