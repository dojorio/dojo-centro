require 'test/unit'
require './magnetico'

class TestMagnetico < Test::Unit::TestCase
  def test_ponteiro_sem_ponto_magnetico
    ponteiro = [0,0]
    magnetos = []
    raio = 1
    assert_equal([0, 0], efeito_magnetico(magnetos, raio, ponteiro))
  end

  def test_outro_ponteiro_sem_ponto_magnetico
    ponteiro = [1,1]
    magnetos = []
    raio = 1
    assert_equal([1, 1], efeito_magnetico(magnetos, raio, ponteiro))
  end

  def test_ponteiro_um_ponto_magnetico_perto
    ponteiro = [1, 1]
    magnetos = [[0, 0]]
    raio = 2
    assert_equal([0, 0], efeito_magnetico(magnetos, raio, ponteiro))
  end
  
  def test_2_ponteiro_um_ponto_magnetico_perto
    ponteiro = [0, 0]
    magnetos = [[1, 1]]
    raio = 2
    assert_equal([1, 1], efeito_magnetico(magnetos, raio, ponteiro))
  end
  
  def test_3_ponteiro_um_ponto_magnetico_perto
    ponteiro = [0, 0]
    magnetos = [[1, 1]]
    raio = 3
    assert_equal([1, 1], efeito_magnetico(magnetos, raio, ponteiro))
  end

  def test_4_ponteiro_um_ponto_magnetico_perto
    ponteiro = [1, 1]
    magnetos = [[2, 2]]
    raio = 2
    assert_equal([2, 2], efeito_magnetico(magnetos, raio, ponteiro))
  end

  def test_5_ponteiro_um_ponto_magnetico_perto
    ponteiro = [1, 1]
    magnetos = []
    raio = 2
    assert_equal([1, 1], efeito_magnetico(magnetos, raio, ponteiro))
  end

  def test_ponteiro_um_ponto_magnetico_longe
    ponteiro = [1, 1]
    magnetos = [[5, 5]]
    raio = 2
    assert_equal([1, 1], efeito_magnetico(magnetos, raio, ponteiro))
  end

  def test_2_ponteiro_um_ponto_magnetico_longe
    ponteiro = [5, 5]
    magnetos = [[1, 1]]
    raio = 2
    assert_equal([5, 5], efeito_magnetico(magnetos, raio, ponteiro))
  end

  def test_3_ponteiro_um_ponto_magnetico_longe
    ponteiro = [0, 0]
    magnetos = [[0, 6]]
    raio = 5
    assert_equal([0, 0], efeito_magnetico(magnetos, raio, ponteiro))
  end

  def test_ponteiro_um_ponto_magnetico_longe_outro_perto
    ponteiro = [0, 0]
    magnetos = [[4, 4], [2, 2]]
    raio = 5
    assert_equal([2, 2], efeito_magnetico(magnetos, raio, ponteiro))
  end
end