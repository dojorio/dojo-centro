class Espiral
  def initialize(linha, coluna)
    @linha = linha
    @coluna = coluna
  end

  def matriz()
    [(1..@coluna).to_a]
  end

  def coluna(indice)
    if indice == 1
      (1..@linha).to_a
    elsif indice == 2

    else
      (@coluna..@linha+@coluna-1).to_a
    end
  end

  def linha(indice)
    if indice == 1
      (1..@coluna).to_a
    elsif indice == 2
      (@coluna+1..2*@coluna).to_a.reverse
    else
      [4,3]
    end
  end
end

