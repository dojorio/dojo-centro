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
  tempo_x = x(tartaruga) - x(tratador)
  tempo_y = y(tartaruga) - y(tratador)

  if tempo_x < 0
    tempo_x= (tempo_x.abs + 2) / 3
  end
  if tempo_y < 0
    if direcao(tartaruga) == 'C'
      tempo_y = (tempo_y.abs + 2) / 3
    else
      tempo_y = tempo_y.abs
    end
  end

  return tempo_x + tempo_y

end