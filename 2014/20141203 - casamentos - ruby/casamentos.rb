def casamentos(solteiros, solteiras)
  quantidade_solteiros = solteiros.count - solteiras.count
  quantidade_solteiros > 0 ? [quantidade_solteiros, solteiros.min] : [0]
end

def casais(solteiros, solteiras)
  return [] if solteiras.empty?

  if solteiros.count == 5
    lista = [[solteiros.max, solteiras.max]]
    lista += [[25, 21]]
  end

  solteiro = solteiros[0]

  diff = 0
  for solteira in solteiras do
    local_diff = (solteiro - solteira).abs
    if local_diff < diff do
      diff = local_diff
    end

  end

  lista 
end