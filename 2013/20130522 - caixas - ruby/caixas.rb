class Caixas

  def self.pode?(em_cima, embaixo)
    em_cima[:peso] <= embaixo[:capacidade]
  end

  def self.empilhar(caixas)
    caixas = caixas.sort_by { |e| -e[:capacidade] }

    pilha = 0
    ultima = { :peso => 0, :capacidade => 1000 }

    caixas.each do |caixa|
      if pode?(caixa, ultima)
        ultima = caixa
        pilha += 1
      end
    end

    pilha
  end
end
