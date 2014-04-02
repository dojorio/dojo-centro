def apagao(ruas)
  if ruas.count < 3 
    return 0
  end

  maior = 0
  for rua in ruas
    if rua[2] > maior
      maior = rua[2]
    end
  end

  return maior
  
end