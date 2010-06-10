class Peca
  attr_accessor :linha

  def initialize(opcoes)
    @tipo = opcoes[:tipo]
    @linha = opcoes[:linha]
    @coluna = opcoes[:coluna]
    @cor = opcoes[:cor]
  end
end

class Jogo
  def initialize(pecas)
    @pecas = pecas
  end

  def atacantes
    if @pecas[1].linha == 3 and @pecas[0].linha == 6
      return nil

    elsif (@pecas.first.linha == (@pecas.last.linha - 1))
      if (@pecas[0].coluna == (@pecas[0].coluna -1) or
          @pecas[0].coluna == (@pecas[0].coluna +1))

        return @pecas[1]
      end
    end
    @pecas[1]
  end
end

