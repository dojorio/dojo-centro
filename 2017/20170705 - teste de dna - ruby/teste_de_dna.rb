def teste_de_dna(dnas)

  if dnas.first.size == 2
    return 'Pai 1'
  end  

  if dnas.last == dnas.first && dnas.last == dnas[1]
    return 'cadim'

  elsif dnas.last == dnas.first 
    return 'Pai 1'

  elsif dnas.last == dnas[1]
    return 'Pai 2'
  end

  return 'cadim'
end