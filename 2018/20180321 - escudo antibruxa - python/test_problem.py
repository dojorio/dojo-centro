#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from problem import *

# https://github.com/jonatasemidio/dojo_problems/blob/master/escudo-anti-bruxas.md
class TestProblem(unittest.TestCase):
    def test_(self):
        criancas = [(0, 0)]
        sal = 0
        self.assertEqual(
            escudo_antibruxa(criancas, sal),
            "BRUXA WINS"
        )


if __name__ == "__main__":
    unittest.main()