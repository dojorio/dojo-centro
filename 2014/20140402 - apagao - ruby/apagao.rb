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

  tamanhos = ruas.map do |rua|
    rua[2]
  end.sort

  total_economizado = 0

  while tamanhos.count > vertices.count - 1
    total_economizado += tamanhos.pop
  end

  return total_economizado
  
end