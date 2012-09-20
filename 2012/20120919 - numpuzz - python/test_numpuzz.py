#coding: utf-8
import unittest
from numpuzz import numpuzz

class TestNumpuzz(unittest.TestCase):

    def test_no_clicks(self):
        esperado = [0,0,0,0,0,0,0,0,0]
        self.assertEquals(esperado, numpuzz([]))

    def test_one_click_4(self):
        esperado = [
            0,1,0,
            1,1,1,
            0,1,0
        ]
        self.assertEquals(esperado, numpuzz([4]))
        
    def test_two_clicks_4(self):
        esperado = [
            0,2,0,
            2,2,2,
            0,2,0
        ]
        self.assertEquals(esperado, numpuzz([4, 4]))

    def test_one_click_0(self):
        esperado = [
            1,1,0,
            1,0,0,
            0,0,0
        ]
        self.assertEquals(esperado, numpuzz([0]))

    def test_one_click_1(self):
        esperado = [
            1,1,1,
            0,1,0,
            0,0,0
        ]
        self.assertEquals(esperado, numpuzz([1]))

    def test_two_clicks_1_for_Juan(self):
        esperado = [
            2,2,2,
            0,2,0,
            0,0,0
        ]
        self.assertEquals(esperado, numpuzz([1, 1]))

    def test_one_click_8(self):
        esperado = [
            0,0,0,
            0,0,1,
            0,1,1
        ]
        self.assertEquals(esperado, numpuzz([8]))

    def test_one_click_7(self):
        esperado = [
            0,0,0,
            0,1,0,
            1,1,1
        ]
        self.assertEquals(esperado, numpuzz([7]))

    def test_one_click_6(self):
        esperado = [
            0,0,0,
            1,0,0,
            1,1,0
        ]
        self.assertEquals(esperado, numpuzz([6]))
        
    def test_one_click_2(self):
        esperado = [
            0,1,1,
            0,0,1,
            0,0,0
        ]
        self.assertEquals(esperado, numpuzz([2]))

    def test_one_click_3(self):
        esperado = [
            1,0,0,
            1,1,0,
            1,0,0
        ]
        self.assertEquals(esperado, numpuzz([3]))

    def test_one_click_5(self):
        esperado = [
            0,0,1,
            0,1,1,
            0,0,1
        ]
        self.assertEquals(esperado, numpuzz([5]))

    def test_one_click_2_one_click_3(self):
        esperado = [
            1,1,1,
            1,1,1,
            1,0,0
        ]
        self.assertEquals(esperado, numpuzz([2, 3]))

    def test_ten_clicks_4(self):
        esperado = [
            0,0,0,
            0,0,0,
            0,0,0
        ]
        self.assertEquals(esperado, numpuzz([4,4,4,4,4,4,4,4,4,4]))
    
    def test_one_click_0_one_click_1_one_click_2(self):
        esperado = [
            2,3,2,
            1,1,1,
            0,0,0
        ]
        self.assertEquals(esperado, numpuzz([0,1,2]))

class QuadradoDeLadoQuadro(unittest.TestCase):
    def test_one_click_5(self):
        esperado = [
            0,1,0,0,
            1,1,1,0,
            0,1,0,0,
            0,0,0,0
        ]
        self.assertEquals(esperado, numpuzz([5], 4))

    def test_one_click_15(self):
        esperado = [
            0,0,0,0,
            0,0,0,0,
            0,0,0,1,
            0,0,1,1
        ]
        self.assertEquals(esperado, numpuzz([15], 4))
    
    def test_one_click_7(self):
        esperado = [
            0,0,0,1,
            0,0,1,1,
            0,0,0,1,
            0,0,0,0
        ]
        self.assertEquals(esperado, numpuzz([7], 4))


unittest.main()
