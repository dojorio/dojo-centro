import NUnit.Framework
import System

    
def fizzbuzz(numero as int):
    resposta = ''
    numero_convertido = numero.ToString()
       
    if numero % 3 == 0 or char('3') in numero_convertido:
         resposta = 'Fizz'
         
    if numero % 5 == 0 or char('5') in numero_convertido:
        resposta += 'Buzz'  
    
    if resposta == '':
        return numero
    else:
        return resposta

def Verificafizzbuzz(numero as int):
    resultado=''
    
    for numero in range (numero):
        resultado+=fizzbuzz(numero+1)
    
    return resultado
    
class FizzBuzzTestsNumber:
    [Test]
    def fizzbuzz_1_deve_retornar_1():
        Assert.AreEqual(1, fizzbuzz(1))
        
    [Test]
    def fizzbuzz_2_deve_retornar_2():
        Assert.AreEqual(2, fizzbuzz(2))

    [Test]
    def fizzbuzz_4_deve_retornar_4():
        Assert.AreEqual(4, fizzbuzz(4))
        

class FizzBuzzTestsFizz:
    [Test]
    def fizzbuzz_3_deve_retornar_Fizz():
        Assert.AreEqual('Fizz', fizzbuzz(3))
        
    [Test]
    def fizzbuzz_6_deve_retornar_Fizz():
        Assert.AreEqual('Fizz', fizzbuzz(6))
        
    [Test]
    def fizzbuzz_13_deve_retornar_Fizz():
        Assert.AreEqual('Fizz', fizzbuzz(13))
        
    [Test]
    def fizzbuzz_23_deve_retornar_Fizz():
        Assert.AreEqual('Fizz', fizzbuzz(23))
        
    [Test]
    def fizzbuzz_31_deve_retornar_Fizz():
        Assert.AreEqual('Fizz', fizzbuzz(31))

    [Test]
    def fizzbuzz_666_deve_retornar_Fizz():
        Assert.AreEqual('Fizz', fizzbuzz(666))
        
class FizzBuzzTestsBuzz:
    [Test]
    def fizzbuzz_5_deve_retornar_Buzz():
        Assert.AreEqual('Buzz', fizzbuzz(5))

    [Test]
    def fizzbuzz_10_deve_retornar_Buzz():
        Assert.AreEqual('Buzz', fizzbuzz(10))

    [Test]
    def fizzbuzz_51_deve_retornar_Buzz():
        Assert.AreEqual('Buzz', fizzbuzz(52))
        
class FizzBuzzTestsFizzBuzz:
    [Test]
    def fizzbuzz_15_deve_retornar_FizzBuzz():
        Assert.AreEqual('FizzBuzz', fizzbuzz(15))
        
    [Test]
    def Verificafizzbuzz_5_deve_retornar_12Fizz4Buzz():
        Assert.AreEqual('12Fizz4Buzz', Verificafizzbuzz(5))
        
        
    