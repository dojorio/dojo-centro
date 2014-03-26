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
  max_passos = 3
  dx = x(tartaruga) - x(tratador)
  dy = y(tartaruga) - y(tratador)


  if dx < 0 && (dx*-1) < max_passos
    return -dx/max_passos +1
  elsif dx < 0
    return -dx/max_passos 
  end
  dx + dy
end