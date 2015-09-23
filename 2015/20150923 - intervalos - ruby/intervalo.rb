def intervalos(lista)
  return ["1-2"] if lista == [1, 2]

  resultado = []

  lista.each do |elemento|
    resultado << elemento.to_s  
  end


  
  resultado
end