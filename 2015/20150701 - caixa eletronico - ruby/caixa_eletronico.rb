def sacar(valor)
  notas = [10, 20, 50, 100]

  if notas.include?(valor) 
    return [valor]
  end

  notas.each do |nota|
    if notas.include?(valor - nota) 
      return [nota, valor - nota]
    end
  end

  [10, 20, 50]

end