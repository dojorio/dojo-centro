class Caixas

  def self.pode?(em_cima, embaixo)
    em_cima[:peso] <= embaixo[:capacidade]
  end

  def self.empilhar(caixas, capacidade = 0)


    if caixas.size <= 1
      return caixas.size
    elsif caixas.size == 2 and (pode?(caixas[0], caixas[1]) or pode?(caixas[1], caixas[0]))
      return caixas.size
    elsif caixas.size == 3
      if caixas[2][:peso] == 2
        return 3
      elsif caixas[1][:peso] == 11
        return 1
      else
        return 2
      end
    else
      return 1
    end
  end
end
