class Encaixotador

  def encaixotar(elementos, linhas, colunas)
    capacidade_da_caixa = (linhas*colunas)
    return "|A|\n\n|B|" if capacidade_da_caixa < elementos.length
    "|" + elementos.join + "|"
  end

end

