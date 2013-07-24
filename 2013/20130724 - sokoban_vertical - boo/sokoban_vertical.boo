import NUnit.Framework from nunit.framework

def sokoban_vertical(largura, blocos, movimentos):

    if largura == blocos:
        return 1
    else:
        return 0

# entrada: largura do campo, blocos, movimentos
#  O
# |T|
#  3, 1, 1 -> 0
class SokobanVerticalTest:
    [Test]
    def comeca_morto():
        Assert.AreEqual(sokoban_vertical(3, 1, 0), 0)

    [Test]
    def morre_fazendo_ponto():
        Assert.AreEqual(sokoban_vertical(1, 1, 0), 1)

    [Test]
    def anda_para_lado_sem_pontos():
        Assert.AreEqual(sokoban_vertical(1, 2, 0), 1)
