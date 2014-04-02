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

  maior = 0
  for rua in ruas
    if rua[2] > maior
      maior = rua[2]
    end
  end

  return maior
  
end