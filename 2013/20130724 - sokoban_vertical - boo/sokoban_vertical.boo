import NUnit.Framework from nunit.framework

def sokoban_vertical(largura, blocos, movimentos):
    return 0

# entrada: largura do campo, blocos, movimentos
#  O
# |T|
#  3, 1, 1 -> 0
class SokobanVerticalTest:
    [Test]
    def comeca_morto():
        Assert.AreEqual(sokoban_vertical(1, 1, 0), 0)

    [Test]
    def morre_fazendo_ponto():
        Assert.AreEqual(sokoban_vertical(1, 1, 1), 1)
