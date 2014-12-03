def casamentos(solteiros, solteiras)
  if solteiras.empty?
    solteiro_moco = solteiros.min
    return [solteiros.count, solteiro_moco]
  elsif solteiros.count >  solteiras.count
    quantidade_solteiros = solteiros.count - solteiras.count
    menor = solteiros.min
    
    return [quantidade_solteiros,menor]
  end

  [0]
end