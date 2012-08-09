#coding:utf-8
import unittest
from troco import troco

class TestTroco(unittest.TestCase):
    def test_troco_1(self):
        self.assertEqual([1], troco(1))
        
    def test_troco_2(self):
        self.assertEqual([2], troco(2))

    def test_troco_3(self):
        self.assertEqual([2, 1], troco(3))

    def test_troco_4(self):
        self.assertEqual([2, 2], troco(4))

    def test_troco_5(self):
        self.assertEqual([5], troco(5))

    def test_troco_6(self):
        self.assertEqual([5, 1], troco(6))
    
    def test_troco_10(self):
        self.assertEqual([10], troco(10))
        
    def test_troco_19(self):
        self.assertEqual([10, 5, 2, 2], troco(19))

    def test_troco_20(self):
        self.assertEqual([20], troco(20))
        
    #def test_troco_50(self):
     #   self.assertEqual([50], troco(50))
        
    def test_troco_1_e_75(self):
        self.assertEqual([1, .50, .25], troco(1.75))
         
    def test_troco_11_com_notas_diferentes(self):
        self.assertEqual([5, 2, 2, 2], troco(11, [10, 5, 2]))

        
unittest.main()

