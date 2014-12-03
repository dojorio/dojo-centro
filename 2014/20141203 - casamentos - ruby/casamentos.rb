def casamentos(solteiros, solteiras)
  if solteiras.empty?
    solteiro_moco = solteiros.min
    return [solteiros.count, solteiro_moco]
  end

  [0]
end