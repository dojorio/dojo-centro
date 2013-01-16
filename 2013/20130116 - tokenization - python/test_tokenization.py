#-*- coding: utf-8 -*-
import unittest
from tokenization import tokenize

class TokenizationTestCase(unittest.TestCase):

	def test_1(self):
		self.assertEqual([('N', '1'), ], tokenize('1'))


unittest.main()