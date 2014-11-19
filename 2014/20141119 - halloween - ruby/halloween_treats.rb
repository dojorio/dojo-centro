def halloween(criancas, doces)
  casas = (1..doces.length).to_a
  total_doces = doces.reduce(:+)

  return casas if total_doces % criancas == 0

  casas.select do |casa|
    doces[casa - 1] / criancas > 0
  end
end