import NUnit.Framework from nunit.framework
import System

def sokoban_vertical(largura as int, blocos as int, movimentos as int):
    if largura == 1:
        return Math.Min(1, blocos)

    movimentos_ideais = 5+((largura*largura) - (4*largura) + 3) / 2
    movimentos_ate_o_inicio = movimentos / movimentos_ideais
    blocos_por_largura = blocos / largura
    return Math.Min(blocos_por_largura, movimentos_ate_o_inicio)


# entrada: largura do campo, blocos, movimentos
#  O
# |T|
#  3, 1, 1 -> 0
class SokobanVerticalTest:
    [Test]
    def comeca_morto():
        Assert.AreEqual(0, sokoban_vertical(3, 1, 0))

    [Test]
    def morre_fazendo_ponto():
        Assert.AreEqual(1, sokoban_vertical(1, 1, 0))

    [Test]
    def anda_para_lado_sem_pontos():
        Assert.AreEqual(1, sokoban_vertical(1, 2, 0))

    [Test]
    def sem_caixa():
        Assert.AreEqual(0, sokoban_vertical(1, 0, 0))

    [Test]
    def tres_caixas_fazendo_uma_linha():
        Assert.AreEqual(1, sokoban_vertical(3, 3, 5))

    [Test]
    def tres_caixas_fazendo_uma_linha_com_movimentos_de_sobra():
        Assert.AreEqual(1, sokoban_vertical(3, 3, 6))

    [Test]
    def tres_caixas_fazendo_duas_linhas():
        Assert.AreEqual(2, sokoban_vertical(3, 6, 10))

    [Test]
    def tres_caixas_fazendo_duas_linhas_com_movimento_faltando():
        Assert.AreEqual(2, sokoban_vertical(3, 9, 10))

    [Test]
    def tres_caixas_fazendo_1_linha_com_movimento_sobrando():
        Assert.AreEqual(1, sokoban_vertical(3, 3, 10))

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

    [Test]
    def sete_caixas_grid_7_com_movimentos_minimos_para_0_ponto():
        Assert.AreEqual(0, sokoban_vertical(7, 7, 13))

    [Test]
    def sete_caixas_grid_7_com_movimentos_minimos_para_1_ponto():
        Assert.AreEqual(1, sokoban_vertical(7, 7, 17))

    [Test]
    def sete_caixas_grid_9_com_movimentos_minimos_para_1_ponto():
        Assert.AreEqual(1, sokoban_vertical(9, 9, 29))

