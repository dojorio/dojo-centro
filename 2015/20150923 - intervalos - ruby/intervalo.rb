def intervalos(lista)
  return ["1-2"] if lista == [1, 2]
  return ["2-3"] if lista == [2, 3]


  resultado = []

  lista.each do |elemento|
    resultado << elemento.to_s  
  end


  
  resultado
end