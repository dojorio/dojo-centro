def halloween(criancas, doces)
  casas = (1..doces.length).to_a
  total_doces = doces.reduce(:+)

  return casas if total_doces % criancas == 0

  pior = nil

  casas.reverse_each do |casa|
    pior ||= casa - 1 if doces[casa - 1] < criancas
  end
  
  casas.delete_at(pior) if pior

  casas
end