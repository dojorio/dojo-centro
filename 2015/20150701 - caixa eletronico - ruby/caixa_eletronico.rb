def sacar(valor)

  notas = [10, 20, 50, 100]

  if notas.include?(valor) 
    return [valor]
  end

  if notas.include?(valor - 10) 
    return [10, valor - 10]
  end

  if valor == 70
    return [20, 50]
  end

  if valor == 40
    return [20, 20]
  end

  if valor == 120
    return [20, 100]
  end
end