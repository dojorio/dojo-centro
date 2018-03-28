#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_a(self):
        expression = "a"
        polonese_posfix_expression = "a"
        
        self.assertEqual(
            transliterate(expression), 
            polonese_posfix_expression
        )

    def test_a_b_plus(self):
        expression = "a+b"
        polonese_posfix_expression = "ab+"
        
        self.assertEqual(
            transliterate(expression), 
            polonese_posfix_expression
        )

    def test_a_c_plus(self):
        expression = "a+c"
        polonese_posfix_expression = "ac+"
        
        self.assertEqual(
            transliterate(expression), 
            polonese_posfix_expression
        )

    def test_a_b_plus_c_plus(self):
        expression = "a+b+c"
        polonese_posfix_expression = "ab+c+"
        
        self.assertEqual(
            transliterate(expression), 
            polonese_posfix_expression
        )

if __name__ == "__main__":
    unittest.main()

