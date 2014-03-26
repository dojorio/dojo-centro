def x(algo)
  algo.first
end

def y(algo)
  algo[1]
end

def direcao(tartaruga)
  tartaruga[2]
end

def pega_tartaruga(tratador, tartaruga)
  dx = x(tartaruga) - x(tratador)
  dy = y(tartaruga) - y(tratador)

  if dx < 0
    return -dx/3+1
  else
    return dx + dy
  end
end