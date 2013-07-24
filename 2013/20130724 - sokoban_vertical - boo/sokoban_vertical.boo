import NUnit.Framework from nunit.framework
import System

def sokoban_vertical(largura as int, blocos as int, movimentos as int):
    if movimentos >= 5:
        movimentos_por_5 = movimentos / 5
        blocos_por_3 = blocos / 3
        return Math.Min(blocos_por_3, movimentos_por_5)
    if largura == 1 and blocos > 0:
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

    [Test]
    def sem_caixa():
        Assert.AreEqual(sokoban_vertical(1, 0, 0), 0)

    [Test]
    def tres_caixas_fazendo_uma_linha():
        Assert.AreEqual(sokoban_vertical(3, 3, 5), 1)

    [Test]
    def tres_caixas_fazendo_uma_linha_com_movimentos_de_sobra():
        Assert.AreEqual(sokoban_vertical(3, 3, 6), 1)

    [Test]
    def tres_caixas_fazendo_duas_linhas():
        Assert.AreEqual(sokoban_vertical(3, 6, 10), 2)

    [Test]
    def tres_caixas_fazendo_duas_linhas_com_movimento_faltando():
        Assert.AreEqual(sokoban_vertical(3, 9, 10), 2)

    [Test]
    def tres_caixas_fazendo_1_linha_com_movimento_sobrando():
        Assert.AreEqual(sokoban_vertical(3, 3, 10), 1)

