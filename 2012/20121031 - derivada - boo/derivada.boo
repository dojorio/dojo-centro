import NUnit.Framework from nunit.framework
import System.Linq.Enumerable from System.Core


# 0x^0 + 0x^1 + 5x^2 + x^3 + 2x^4
#  0  1  2  3  4
# [0, 0, 5, 1, 2]
def derivada(list as (int)):
    
    return ((0,) if list.Length == 1 else list.Select({ item, i | i * item }).Skip(1))
        
    
class DerivadaTest:
    [Test]
    def constante_1():
        # derivada(1x^0) = 0
        resultado = derivada((1,))
        Assert.AreEqual((0,), resultado)

    [Test]
    def constante_5():
        # derivada(5x^0) = 0
        resultado = derivada((5,))
        Assert.AreEqual((0,), resultado)
    
    [Test]
    def monomio_grau_1():
        # 0x^0 + 1x^1 = x
        # derivada(0x^0 + x^1) = 1
        resultado = derivada((0, 1))
        Assert.AreEqual((1,), resultado)
    
    [Test]
    def monomio_grau_1_com_coeficiente_2():
        # 0x^0 + 2x^1 = x
        # derivada(0x^0 + 2x^1) = 2
        resultado = derivada((0, 2))
        Assert.AreEqual((2,), resultado) 
    
    [Test]
    def monomio_grau_1_com_coeficiente_2_e_constante_5():
        # 5x^0 + 2x^1 = x
        # derivada(5x^0 + 2x^1) = 2
        resultado = derivada((5, 2))
        Assert.AreEqual((2,), resultado)

    [Test]
    def polinomio_2o_grau_coeficiente_3():
        # derivada(0x^0 + 0x^1 + 3x^2) = 0, 6
        resultado = derivada((0, 0, 3))
        Assert.AreEqual((0, 6), resultado)

    [Test]
    def polinomio_2o_grau_coeficiente_4():
        # derivada(0x^0 + 0x^1 + 4x^2) = 0, 8
        resultado = derivada((0, 0, 4))
        Assert.AreEqual((0, 8), resultado)

    [Test]
    def polinomio_2o_grau_coeficiente_16():
        # derivada(0x^0 + 0x^1 + 16x^2) = 0, 32
        resultado = derivada((0, 0, 16))
        Assert.AreEqual((0, 32), resultado)


    [Test]
    def polinomio_2o_grau_coeficiente_2_1o_grau_coeficiente_1():
        # derivada(0x^0 + 1x^1 + 2x^2) = 1, 4
        resultado = derivada((0, 1, 2))
        Assert.AreEqual((1, 4), resultado)

