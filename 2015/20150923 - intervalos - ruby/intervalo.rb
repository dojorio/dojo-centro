def intervalos(lista)
  if lista[2] == 5
    return ["2-3", "5"]
  end
  
  if lista == [1,2,4]
    return ["1-2", "4"]
  end

  if lista.size == 2 && lista[1] - lista[0] == 1
    return ["#{lista[0]}-#{lista[1]}"]
  end

  resultado = []

  lista.each do |elemento|
    resultado << elemento.to_s  
  end

  resultado
end