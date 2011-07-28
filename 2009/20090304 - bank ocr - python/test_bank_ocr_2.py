import unittest
from bank_ocr_2 import ocr, _split_digitos, checksum, check_account


class TestBankOcr(unittest.TestCase):
    def test_ocr0(self):
        entrada = '''\
 _ 
| |
|_|'''
        self.assertEquals('0', ocr(entrada))

    def test_ocr1(self):
        entrada = '''\
   
  |
  |'''
        self.assertEquals('1', ocr(entrada))

    def test_ocr2(self):
        entrada = '''\
 _ 
 _|
|_ '''
        self.assertEquals('2', ocr(entrada))

    def test_ocr3(self):
        entrada = '''\
 _ 
 _|
 _|'''
        self.assertEquals('3', ocr(entrada))

    def test_ocr4(self):
        entrada = '''\
   
|_|
  |'''
        self.assertEquals('4', ocr(entrada))

    def test_ocr5(self):
        entrada = '''\
 _ 
|_ 
 _|'''
        self.assertEquals('5', ocr(entrada))
        
    def test_ocr6(self):
        entrada = '''\
 _ 
|_ 
|_|'''
        self.assertEquals('6', ocr(entrada))

    def test_ocr7(self):
        entrada = '''\
 _ 
  |
  |'''
        self.assertEquals('7', ocr(entrada))

    def test_ocr8(self):
        entrada = '''\
 _ 
|_|
|_|'''
        self.assertEquals('8', ocr(entrada))
        
    def test_ocr9(self):
        entrada = '''\
 _ 
|_|
 _|'''
        self.assertEquals('9', ocr(entrada))


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

        self.assertEquals([dois, nove], _split_digitos(entrada))
        
    def test_ocr_dois_digitos_29(self):
        entrada = '''\
 _  _ 
 _||_|
|_  _|'''
        self.assertEquals('29', ocr(entrada))


    def test_ocr_dois_digitos_35(self):
        entrada = '''\
 _  _ 
 _||_ 
 _| _|'''
        self.assertEquals('35', ocr(entrada))


    def test_ocr_tres_digitos_351(self):
        entrada = '''\
 _  _    
 _||_   |
 _| _|  |'''
        self.assertEquals('351', ocr(entrada))
    
    def test_ocr_multiplas_contas(self):
        accounts = """\
 _  _  _  _  _  _  _  _  _ 
| || || || || || || || || |
|_||_||_||_||_||_||_||_||_|

                           
  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |
"""
  
        result = """\
000000000
111111111"""

        self.assertEqual(ocr(accounts), result)

        
class TestChecksum(unittest.TestCase):

    def test_checksum_0(self):
        account = 345882865
        self.assertEqual(checksum(account), 0)

    def test_checksum_1(self):
        account = 345882866
        self.assertEqual(checksum(account), 1)

    def test_checksum_7(self):
        account = 123456769
        self.assertEqual(checksum(account), 7)
    
    def test_valid_account(self):
        account = 123456789
        self.assertEqual(check_account(account), True)
    
    def test_invalid_account(self):
        account = 123456769
        self.assertEqual(check_account(account), False)

class TestParseMultipleAccounts(unittest.TestCase):

    def test_multiple_accounts(self):
        accounts = """\
 _  _  _  _  _  _  _  _    
| || || || || || || ||_   |
|_||_||_||_||_||_||_| _|  |
                           
    _  _  _  _  _  _     _ 
|_||_|| || ||_   |  |  | _ 
  | _||_||_||_|  |  |  | _|
                           
 _  _  _  _  _  _  _  _  _ 
| || || || || || || ||_   |
|_||_||_||_||_||_||_| _|  |
                           """
        result = """\
000000051
49006771? ILL
000000057 ERR"""
        
        self.assertEqual(ocr(accounts, validate=True), result)
 
if __name__ == '__main__':
    unittest.main()
