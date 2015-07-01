def sacar(valor)

  notas = [10, 20, 50, 100]

  if notas.include?(valor) 
    return [valor]
  end

  if valor == 30
    return [10, 20]
  end

end