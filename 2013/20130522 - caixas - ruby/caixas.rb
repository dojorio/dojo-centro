class Caixas

  INFINITO = 1.0/0

  def self.pode?(em_cima, capacidade)
    em_cima[:peso] <= capacidade
  end

  def self.empilhar(caixas)
    caixas = caixas.sort_by { |e| -e[:capacidade] }

    pilha = 0
    capacidade_total = INFINITO

    caixas.each do |caixa|
      if pode?(caixa, capacidade_total)
        capacidade_total = [capacidade_total - caixa[:peso], caixa[:capacidade]].min
        pilha += 1
      end
    end

    pilha
  end
end
