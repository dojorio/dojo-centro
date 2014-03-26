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
  (x(tartaruga) - x(tratador) + y(tartaruga) - y(tratador)).abs
end