import unittest
from bank_ocr import *

class BankOcrTest(unittest.TestCase):
    def test_ocr1(self):
        entrada = '''\
   
  |
  |'''
        self.assertEquals(1, ocr(entrada))

    def test_ocr2(self):
        entrada = '''\
 _ 
 _|
|_ '''
        self.assertEquals(2, ocr(entrada))

    def test_ocr3(self):
        entrada = '''\
 _ 
 _|
 _|'''
        self.assertEquals(3, ocr(entrada))

    def test_ocr4(self):
        entrada = '''\
   
|_|
  |'''
        self.assertEquals(4, ocr(entrada))

    def test_ocr5(self):
        entrada = '''\
 _ 
|_ 
 _|'''
        self.assertEquals(5, ocr(entrada))
        
    def test_ocr6(self):
        entrada = '''\
 _ 
|_ 
|_|'''
        self.assertEquals(6, ocr(entrada))

    def test_ocr7(self):
        entrada = '''\
 _ 
  |
  |'''
        self.assertEquals(7, ocr(entrada))

    def test_ocr8(self):
        entrada = '''\
 _ 
|_|
|_|'''
        self.assertEquals(8, ocr(entrada))
        
    def test_ocr9(self):
        entrada = '''\
 _ 
|_|
 _|'''
        self.assertEquals(9, ocr(entrada))


    # dois digitos

    def test_split_digitos(self):
        entrada = '''\
 _  _ 
 _||_|
|_  _|'''

        dois = '''\
 _ 
 _|
|_ '''

        nove = '''\
 _ 
|_|
 _|'''

        self.assertEquals([dois, nove], split_digitos(entrada))
        
    def test_ocr_dois_digitos_29(self):
        entrada = '''\
 _  _ 
 _||_|
|_  _|'''
        self.assertEquals(29, ocr(entrada))


    def test_ocr_dois_digitos_35(self):
        entrada = '''\
 _  _ 
 _||_ 
 _| _|'''
        self.assertEquals(35, ocr(entrada))


    def test_ocr_tres_digitos_351(self):
        entrada = '''\
 _  _    
 _||_   |
 _| _|  |'''
        self.assertEquals(351, ocr(entrada))
        

if __name__ == '__main__':
    unittest.main()
