#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_a(self):
        expression = "a"
        polonese_posfix_expression = "a"
        
        self.assertEqual(
            polonese_posfix_expression,
            transliterate(expression)
        )

    def test_a_b_plus(self):
        expression = "a+b"
        polonese_posfix_expression = "ab+"
        
        self.assertEqual(
            polonese_posfix_expression,
            transliterate(expression) 
            
        )

    def test_a_c_plus(self):
        expression = "a+c"
        polonese_posfix_expression = "ac+"
        
        self.assertEqual(
            polonese_posfix_expression,
            transliterate(expression) 
        )

    def test_a_b_plus_c_plus(self):
        expression = "a+b+c"
        polonese_posfix_expression = "ab+c+"
        
        self.assertEqual(
            polonese_posfix_expression,
            transliterate(expression)
        )

    def test_a_c_plus_b_plus(self):
        #             01234
        expression = "a+c+b"
        polonese_posfix_expression = "ac+b+"
       
        self.assertEqual(
            polonese_posfix_expression,
            transliterate(expression)
        )

    def test_a_c_minus_b_plus(self):
        #             01234
        expression = "a-c+b"
        polonese_posfix_expression = "ac-b+"
       
        self.assertEqual(
            polonese_posfix_expression,
            transliterate(expression)
        )

    def test_ab_plius_c_plus_d_plus(self):
        #             01234
        expression = "a+b+c+d"
        polonese_posfix_expression = "ab+c+d+"
       
        self.assertEqual(
            polonese_posfix_expression,
            transliterate(expression)
        )

    def test_ab_plius_c_plus_with_parenthesis(self):
        #             01234
        expression = "(a+b)+c"
        polonese_posfix_expression = "ab+c+"
       
        self.assertEqual(
            polonese_posfix_expression,
            transliterate(expression)
        )

    def test_ab_plius_c_plus_with_parenthesis_again(self):
        #             01234
        expression = "a+(b+c)"
        polonese_posfix_expression = "abc++"
       
        self.assertEqual(
            polonese_posfix_expression,
            transliterate(expression)
        )

    def test_ab_plius_d_plus_with_parenthesis_again(self):
        #             01234
        expression = "a+(b+d)"
        polonese_posfix_expression = "abd++"
       
        self.assertEqual(
            polonese_posfix_expression,
            transliterate(expression)
        )

    def test_ab_plius_c_plus_with_parenthesis(self):
        #             01234
        expression = "(a+b)+c"
        polonese_posfix_expression = "ab+c+"
       
        self.assertEqual(
            polonese_posfix_expression,
            transliterate(expression)
        )

    def test_ab_plus_with_parenthesis(self):
        #             01234
        expression = "(a+b)"
        polonese_posfix_expression = "ab+"
       
        self.assertEqual(
            polonese_posfix_expression,
            transliterate(expression)
        )

    def test_ab_plus_c_with_parenthesis(self):
        #             01234
        expression = "(a+b+c)"
        polonese_posfix_expression = "ab+c+"
       
        self.assertEqual(
            polonese_posfix_expression,
            transliterate(expression)
        )



    def test_ab_plus_c_plus_d(self):
        #             01234
        expression = "a+b+c+d"
        polonese_posfix_expression = "ab+c+d+"
       
        self.assertEqual(
            polonese_posfix_expression,
            transliterate(expression)
        )
if __name__ == "__main__":
    unittest.main()

