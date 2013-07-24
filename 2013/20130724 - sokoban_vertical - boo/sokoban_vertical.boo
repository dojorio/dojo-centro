import NUnit.Framework from nunit.framework
import System

def sokoban_vertical(largura as int, blocos as int, movimentos as int):
    movimentos_ideais = largura * 2 - 1

    if movimentos >= movimentos_ideais:
        movimentos_ate_o_inicio = movimentos / movimentos_ideais
        blocos_por_largura = blocos / largura
        return Math.Min(blocos_por_largura, movimentos_ate_o_inicio)
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

    [Test]
    def tres_caixas_grid_5():
        Assert.AreEqual(0, sokoban_vertical(5, 3, 10))

    [Test]
    def cinco_caixas_grid_5_com_minimo():
        Assert.AreEqual(1, sokoban_vertical(5, 5, 9))

    [Test]
    def cinco_caixas_grid_5_com_movimentos_extras():
        Assert.AreEqual(1, sokoban_vertical(5, 10, 10))

    [Test]
    def cinco_caixas_grid_5_com_movimentos_minimos_para_2_pontos():
        Assert.AreEqual(2, sokoban_vertical(5, 10, 18))
