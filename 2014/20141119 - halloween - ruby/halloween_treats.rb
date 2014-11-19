def halloween(criancas, doces)
  casas = (1..doces.length).to_a
  total_doces = doces.reduce(:+)

  return casas if total_doces % criancas == 0

  pior = nil

  casas.reverse.each do |casa|
    pior ||= casa - 1 if doces[casa - 1] / criancas == 0
  end
  pior ||= casas.length - 1

  casas.delete_at(pior)

  casas
end