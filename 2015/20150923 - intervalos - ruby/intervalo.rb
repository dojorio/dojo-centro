def intervalos(lista)
  resultado = []

  if lista.size > 1 && lista[1] - lista[0] == 1
    resultado << "#{lista[0]}-#{lista[1]}"
    resultado << lista[2].to_s if lista.size == 3
  else
    resultado << lista[0].to_s

    if lista.size == 3 && lista[2] - lista[1] == 1
      resultado << "#{lista[1]}-#{lista[2]}"
    elsif lista.size > 1
      resultado << lista[1].to_s
    end
  end

  resultado
end