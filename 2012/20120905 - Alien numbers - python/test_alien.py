#coding: utf-8
import unittest
from alien import translate, to_decimal, to_base

class TestAlien(unittest.TestCase):

    def test_translate_01_ab_returns_b(self):
        self.assertEqual(translate("1", "01", "ab"), "b")

    def test_translate_01_ab_returns_a(self):
        self.assertEqual(translate("0", "01", "ab"), "a")
    
    def test_translate_01_ab_returns_aa(self):
        self.assertEqual(translate("00", "01", "ab"), "a")
        
    def test_translate_012_abc_returns_aac(self):
        self.assertEqual(translate("002", "012", "abc"), "c")

    def test_translate_0123_ab_returns_bb(self):
        # a  b ba bb
        # 0  1  2  3
        self.assertEqual(translate("3", "0123", "ab"), "bb") 

    def test_translate_b_abc(self):
        self.assertEqual(to_decimal("b", "abc"), 1)

    def test_translate_c_abc(self):
        self.assertEqual(to_decimal("c", "abc"), 2)

    def test_translate_cc_abc(self):
        #c * 3 + c
        #2 * 3 + 2
        self.assertEqual(to_decimal("cc", "abc"), 8)
        
        
    def test_translate_2_abc(self):
        self.assertEqual(to_base(2, "abc"), "c")


    def test_translate_1_abc(self):
        self.assertEqual(to_base(1, "abc"), "b")

    def test_translate_7_abc(self):
        self.assertEqual(to_base(7, "abc"), "cb")

    def test_translate_14_abc(self):
        self.assertEqual(to_base(14, u"0123456789abcdéf"), u"é")


        
unittest.main()
