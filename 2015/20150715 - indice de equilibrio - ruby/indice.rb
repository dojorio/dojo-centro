def equilibrio(lista)
  if lista.size == 1
    return 0
  end

  if lista.size == 2
    if lista[0] == 0
      return 1
    end

    if lista[1] == 0
      return 0
    end

    return -1
  end

  0     
end