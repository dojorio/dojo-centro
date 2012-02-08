import NUnit.Framework from nunit.framework

def ponto_medio(p1 as (double), p2 as (double)):
    x = (p1[0]+p2[0])/2
    y = (p1[1]+p2[1])/2
    return (x, y)

def tres_triangulos_seguintes(triangulo as ((double))):
    a, b, c = triangulo
    
    triangulos= [
        (a, ponto_medio(a, b), ponto_medio(a, c)),
        (b, ponto_medio(a, b), ponto_medio(b, c)),
        (c, ponto_medio(a, c), ponto_medio(b, c)),
    ]
        
    return triangulos

class PontoMedioTest:
    [Test]
    def ponto_medio_entre_dois_pontos():
        pontos = ((0.0, 0.0), (0.0, 10.0))
        Assert.AreEqual((0.0, 5.0), ponto_medio(pontos[0], pontos[1]))
    
    [Test]
    def ponto_medio_entre_dois_pontos2():
        pontos = ((0.0, 0.0), (10.0, 0.0))
        Assert.AreEqual((5.0, 0.0), ponto_medio(pontos[0], pontos[1]))   
        
    [Test]
    def ponto_medio_entre_dois_pontos3():
        pontos = ((0.0, 0.0), (11.0, 0.0))
        Assert.AreEqual((5.5, 0.0), ponto_medio(pontos[0], pontos[1]))        
        

class Triangulos:
    [Test]
    def test_tres_primeiros_triangulos():
        a = (0.0,0.0)
        b = (3.0,0.0)
        c = (3.0,3.0)
        triangulo = (a, b, c)
        triangulos= [
            (a, ponto_medio(a, b), ponto_medio(a, c)),
            (b, ponto_medio(a, b), ponto_medio(b, c)),
            (c, ponto_medio(a, c), ponto_medio(b, c)),
        ]
        
        Assert.AreEqual(triangulos, tres_triangulos_seguintes((triangulo)))
        
    [Test]
    def test_tres_primeiros_triangulos():
        a = (0.0,0.0)
        b = (3.0,0.0)
        c = (3.0,3.0)
        triangulo = (a, b, c)
        triangulos= [
            (a, ponto_medio(a, b), ponto_medio(a, c)),
            (b, ponto_medio(a, b), ponto_medio(b, c)),
            (c, ponto_medio(a, c), ponto_medio(b, c)),
        ]

        t1, t2, t3 = tres_triangulos_seguintes((triangulo))
        
        Assert.AreEqual(triangulos, tres_triangulos_seguintes((triangulo)))
