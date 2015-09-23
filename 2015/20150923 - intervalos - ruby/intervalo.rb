def intervalos(lista)
  if lista.size == 2 && lista[1] - lista[0] == 1
    return ["#{lista[0]}-#{lista[1]}"]
  end

  resultado = []

  lista.each do |elemento|
    resultado << elemento.to_s  
  end

  resultado
end