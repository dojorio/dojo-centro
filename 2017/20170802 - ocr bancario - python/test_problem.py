#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://www.dojopuzzles.com/problemas/exibe/ocr-bancario/

#     _  _       _   _  _   _   _
#  |  _| _| |_| |_  |_   | |_| |_|
#  | |_  _|   |  _| |_|  | |_|  _|



import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def test_1(self):
        source = [
          "   ",
          "  |",
          "  |"
        ]
        self.assertEqual(ocr(source), 1)

    def test_2(self):
        source = [
          " _ ",
          " _|",
          "|_ "
        ]
        self.assertEqual(ocr(source), 2)

    def test_3(self):
        source = [
          " _ ",
          " _|",
          " _|"
        ]
        self.assertEqual(ocr(source), 3)    

    def test_4(self):
        source = [
          "   ",
          "|_|",
          "  |"
        ]
        self.assertEqual(ocr(source), 4)    

    def test_5(self):
        source = [
          " _ ",
          "|_ ",
          " _|"
        ]
        self.assertEqual(ocr(source), 5)

    def test_6(self):
        source = [
          " _ ",
          "|_ ",
          "|_|"
        ]
        self.assertEqual(ocr(source), 6)

    def test_7(self):
        source = [
          " _ ",
          "  |",
          "  |"
        ]
        self.assertEqual(ocr(source), 7)

    def test_8(self):
        source = [
          " _ ",
          "|_|",
          "|_|"
        ]
        self.assertEqual(ocr(source), 8)

    def test_9(self):
        source = [
          " _ ",
          "|_|",
          " _|"
        ]
        self.assertEqual(ocr(source), 9)

    def test_0(self):
        source = [
          " _ ",
          "| |",
          "|_|"
        ]
        self.assertEqual(ocr(source), 0)

    def test_10(self):
        source = [
          "     _ ",
          "  | | |",
          "  | |_|"
        ]
        self.assertEqual(ocr(source), 10)


if __name__ == "__main__":
    unittest.main()
