def casamentos(solteiros, solteiras)
  solteiro_moco = solteiros.min
 
  if solteiras.empty?
    return [solteiros.count, solteiro_moco]
  elsif solteiros.count >  solteiras.count
    quantidade_solteiros = solteiros.count - solteiras.count
    return [quantidade_solteiros,solteiro_moco]
  end

  [0]
end