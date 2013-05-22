class Caixas

  def self.pode?(em_cima, embaixo)
    em_cima[:peso] <= embaixo[:capacidade]
  end

  def self.empilhar(caixas)
    nao_empilhaveis = 0

    if caixas.size == 1
      return 1
    elsif pode?(caixas[0], caixas[1]) or pode?(caixas[1], caixas[0])
      return 2
    else
      return 1
    end
  end
end
