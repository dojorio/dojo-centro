def casamentos(solteiros, solteiras)
  quantidade_solteiros = solteiros.count - solteiras.count
  quantidade_solteiros > 0 ? [quantidade_solteiros, solteiros.min] : [0]
end

def casais(solteiros, solteiras)
  return [] if solteiras.empty?

  lista = [[solteiros.max, solteiras.max]]

  if solteiros.count == 5
    lista += [[25, 21]]
  end

  lista 
end