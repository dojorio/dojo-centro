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
  if direcao(tartaruga) == 'D'
    return x(tartaruga) - x(tratador)
  elsif direcao(tartaruga) == 'C'
    return y(tartaruga) - y(tratador)
  end
end