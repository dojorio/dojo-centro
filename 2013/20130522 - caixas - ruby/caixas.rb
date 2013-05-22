class Caixas

  def self.empilhar(caixas)
    caixas.each do |caixa|
      if caixa[:capacidade] == 0
        return 1
      end
    end

    caixas.size
  end

end
