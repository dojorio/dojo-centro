def intervalos(lista)
  resultado = []

  if lista.size == 1
    resultado << lista[0].to_s
  end

  if lista.size == 2 
    if lista[1] - lista[0] == 1
      resultado << "#{lista[0]}-#{lista[1]}"
    else
      resultado << lista[0].to_s
      resultado << lista[1].to_s
    end
  end

  if lista.size == 3
    if lista[2] - lista[1] == 1
      if lista[1] - lista[0] == 1
        resultado << "#{lista[0]}-#{lista[2]}"
      else
        resultado << lista[0].to_s
        resultado << "#{lista[1]}-#{lista[2]}"
      end
    else
      resultado = intervalos([lista[0], lista[1]])

      resultado << lista[2].to_s
    end
  end
  
  resultado
end