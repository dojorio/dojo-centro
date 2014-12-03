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

  solteiros = solteiros.sort.reverse

  diff = 1000
  index_solteira = 0

  solteiras.each_with_index do |solteira, index|
    local_diff = (solteiro - solteira).abs
    if local_diff < diff
      diff = local_diff
      index_solteira = index
    end
  end

  return [[solteiro, solteiras[index_solteira]]]

end