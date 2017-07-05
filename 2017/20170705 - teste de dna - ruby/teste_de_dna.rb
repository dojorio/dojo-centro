def teste_de_dna(dnas)

  if dnas.last == dnas.first && dnas.last == dnas[1]
    return 'cadim'

  if dnas.last == dnas.first 
    return 'Pai 1'

  elsif dnas.last == dnas[1]
    return 'Pai 2'
  end

  return 'cadim'
end