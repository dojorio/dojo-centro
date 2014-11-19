def halloween(criancas, doces)
  casas = (1..doces.length).to_a
  total_doces = doces.reduce(:+)

  return casas if total_doces % criancas == 0

  return [1] if doces.first / criancas > 0
  return [2] if doces.last  / criancas > 0

  []
end