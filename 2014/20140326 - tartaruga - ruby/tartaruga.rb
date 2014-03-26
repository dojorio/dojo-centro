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
  if direcao(tartaruga) == 'C'
    eixo = x
  else
    eixo = y
  end
  eixo(tartaruga) - eixo(tratador)
end