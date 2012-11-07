import NUnit.Framework from nunit.framework


# 0x^0 + 0x^1 + 5x^2 + x^3 + 2x^4
#  0  1  2  3  4
# [0, 0, 5, 1, 2]

def integral(list as (int)):
    resultado = [0, ]
    for i in range(1, list.Length):
        resultado.Add(list[i] / (i * 1.0))
    return resultado

class DerivadaTest:
    [Test]
    def constante_1():
        # integral(1x^0) = 0
        resultado = integral((1,))
        Assert.AreEqual((0, 1), resultado)

    [Test]
    def constante_3():
        # integral(3x^0) = 3
        resultado = integral((3,))
        Assert.AreEqual((0, 3), resultado)

    [Test]
    def primeiro_grau_coeficiente_3():
        # integral(0x^0 + 3x^1) = (3x^2) / 2
        resultado = integral((0, 3))
        Assert.AreEqual((0, 0, 3.0/2), resultado)

    [Test]
    def primeiro_grau_coeficientes_1_e_10():
        # integral(1x^0 + 10x^1) = 1 + (10x^2) / 2
        resultado = integral((1, 10))
        Assert.AreEqual((0, 1, 10.0/2), resultado)

    [Test]
    def segundo_grau_coeficiente_5():
        # integral(0x^0 + 0x^1 + 5x^2) = (5x^3) / 3
        resultado = integral((0, 0, 5))
        Assert.AreEqual((0, 0, 0, 5.0/3), resultado)

    [Test]
    def primeiro_grau_coeficientes_2_e_8():
        # integral(2x^1 + 8x^2) = (2x^2) / 2 + (8x^3) / 3
        resultado = integral((0, 2, 8))
        Assert.AreEqual((0, 0, 2.0/2, 8.0/3), resultado)
