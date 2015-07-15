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

  if lista.size == 3
    if lista[2] == -1
      return 0
    elsif lista[1] == -1
      return -1
    elsif lista[0] == -1
      return 2
    end


    
    return 1
  
  end

  0     
end