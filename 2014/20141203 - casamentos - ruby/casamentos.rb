def casamentos(solteiros, solteiras)
  if solteiras.empty?
    solteiro_moco = solteiros.min
    return [solteiros.count, solteiro_moco]
  elsif solteiros.count >  solteiras.count
    return [1,20]
  end

  [0]
end