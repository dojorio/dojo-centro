import unittest

from OCR import *
from textwrap import dedent

class TesteOCR(unittest.TestCase):
    def test_1(self):
        char = """\
   
  |
  |"""
        num = conversor(char)
        self.assertEqual(num, 1)

    def test_2(self):
        char = """\
 _ 
 _|
|_ """
        num = conversor(char)
        self.assertEqual(num, 2)
        
      
    def test_3(self):
        char = """\
 _ 
 _|
 _|"""
        num = conversor(char)
        self.assertEqual(num, 3)

    def test_4(self):
        char = """\
   
|_|
  |"""
        num = conversor(char)
        self.assertEqual(num, 4)
        
    def test_5(self):
        char = """\
 _ 
|_ 
 _|"""
        num = conversor(char)
        self.assertEqual(num, 5)

    def test_11(self):
        char = """\
      
  |  |
  |  |"""
        num = conversor(char)
        self.assertEqual(num, 11)
        
    def test_55(self):
        char = """\
  _  _   
 |_ |_ 
  _| _|"""
        num = conversor(char)
        self.assertEqual(num, 55)
        
unittest.main()