class Caixas

  def self.empilhar(caixas)
    nao_empilhaveis = 0

    caixas.each do |caixa|
      if caixa[:capacidade] == 0
        nao_empilhaveis += 1
      end
    end

    if nao_empilhaveis == caixas.size
      1
    else
      caixas.size
    end
  end

end
