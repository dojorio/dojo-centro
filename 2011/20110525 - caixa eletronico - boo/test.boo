import NUnit.Framework
import System

private def existe_nota_de(valor):
    return valor in (2, 5, 10, 20, 50, 100)
    
def sacar(valor as int) as (int):
    if existe_nota_de(valor):
        return (valor,) 
    
    if valor <= 0:
        raise EntradaInconsistente() 
    
    return (20, 20) if valor == 40  
    
    if valor != 1: 
        if valor > 100:
            return (100,) + sacar(valor - 100)
        elif valor > 50:
            return (50,) + sacar(valor - 50)
        elif valor > 20:
            return (20,) + sacar(valor - 20)
        elif valor > 10:
            return (10,) + sacar(valor - 10)
        elif valor > 5:
            return (5,) + sacar(valor - 5)
        elif valor > 2:
            return (2,) + sacar(valor - 2)
        
    raise ValorInexistente()    
    
    

class ValorInexistente(Exception):
    pass

class EntradaInconsistente(Exception):
    pass

class CasosPositivosTest:
    [Test]
    def sacar_o_valor_de_uma_nota_deveria_retornar_a_nota():
        for nota in (2, 5, 10, 20, 50, 100):
            CollectionAssert.AreEquivalent((nota,), sacar(nota))

    [Test]
    def sacar_7_deveria_retornar_uma_nota_de_2_e_uma_de_5():
        CollectionAssert.AreEquivalent((2, 5), sacar(7))

    [Test]
    def sacar_12_deveria_retornar_uma_nota_de_2_e_uma_de_10():
        CollectionAssert.AreEquivalent((2, 10), sacar(12))
        
    [Test]
    def sacar_22_deveria_retornar_uma_nota_de_2_e_uma_de_20():
        CollectionAssert.AreEquivalent((2, 20), sacar(22))
        
    [Test]
    def sacar_2_e_outra_nota_deveria_retornar_uma_nota_de_2_e_a_outra_nota():
        for nota in (5, 10, 20, 50, 100):
            valor = nota + 2
            CollectionAssert.AreEquivalent((2, nota), sacar(valor))
    [Test]
    def sacar_6_deveria_retornar_tres_notas_de_2():
        CollectionAssert.AreEquivalent((2, 2, 2), sacar(6))

    [Test]
    def sacar_9_deveria_retornar_duas_notas_de_2_e_uma_de_5():
        CollectionAssert.AreEquivalent((2, 2, 5), sacar(9))

    [Test]
    def sacar_15_deveria_retornar_uma_nota_de_10_e_uma_de_5():
        CollectionAssert.AreEquivalent((5, 10), sacar(15))
        
    [Test]
    def sacar_40_deveria_retornar_duas_notas_de_20():
        CollectionAssert.AreEquivalent((20, 20), sacar(40))
            
class CasosDegeneradosTest:
    [Test]
    def sacar_um_real_deveria_retornar_erro():
        Assert.Throws[of ValorInexistente]({sacar(1)})
      
    [Test]
    def sacar_tres_reais_deveria_retornar_erro():
        Assert.Throws[of ValorInexistente]({sacar(3)})
    
        
    [Test]
    def sacar_zero_reais_deveria_retornar_erro():
        Assert.Throws[of EntradaInconsistente]({sacar(0)})
        
        
    [Test]
    def sacar_valor_negativo_deveria_retornar_erro():
        Assert.Throws[of EntradaInconsistente]({sacar(-1)})
        
    [Test]
    def sacar_quatro_reais_deveria_retornar_duas_notas_de_dois():
       CollectionAssert.AreEquivalent((2, 2), sacar(4))
       
    
       
