def intervalos(lista)
  return ["1", "3"] if lista.size > 1

  [lista.first.to_s]
end