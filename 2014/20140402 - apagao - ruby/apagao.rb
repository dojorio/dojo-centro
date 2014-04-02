def apagao(ruas)
  vertices = []

  for rua in ruas
    vertices.push(rua[0])
    vertices.push(rua[1])
  end

  vertices = vertices.uniq

  if ruas.count <= vertices.count - 1
    return 0
  end

  maior = ruas.map do |rua|
    rua[2]
  end.max

return maior


  tamanhos = []
  ruas.each do |rua|
    tamanhos.push(rua[2])
  end

  if tamanhos.uniq.count == 1
    return ruas[0][2] * (ruas.count - 1)
  end

  
  
end