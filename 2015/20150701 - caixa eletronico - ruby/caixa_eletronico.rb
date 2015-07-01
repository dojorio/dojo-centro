def sacar(valor)

  notas = [10, 20, 50, 100]

  if valor == 100
    return notas[3]
  end
  if valor == 50
    return notas[2]
  end

  if valor == 20 
    return notas[1]
  end

  if valor == 30
    return notas[0,1]
  end

  return notas[0]
end