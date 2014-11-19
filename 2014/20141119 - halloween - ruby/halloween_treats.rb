def halloween(criancas, doces)
  casas = (1..doces.length).to_a
  total_doces = doces.reduce(:+)

  return casas if total_doces % criancas == 0

  resultado = casas.select do |casa|
    doces[casa - 1] / criancas > 0
  end

  melhor = 0

  if resultado.empty? && total_doces / criancas > 0
    total_doces = 0

    casas.each do |casa|
      total_doces += doces[casa - 1]
      resultado << casa

      if total_doces / criancas == 0
        melhor = casa - 1
      end
    end
  end

  resultado
end