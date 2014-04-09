def apagao(ruas)
  vertices = []

  for rua in ruas
    vertices.push(rua[0])
    vertices.push(rua[1])
  end

  vertices = vertices.uniq

  sorted_coordenadas_de_ruas = ruas.map do |rua|
    if rua[0] > rua[1]
      rua[0] = rua[0] ^ rua[1]
      rua[1] = rua[1] ^ rua[0]
      rua[0] = rua[0] ^ rua[1]
    end
    rua
  end.sort

  foi = []
  total_economizado = sorted_coordenadas_de_ruas.reduce(0) do |memo, rua|
    if foi.include?(rua.slice(0,2))
      memo + rua[2] 
    else
      foi.push(rua.slice(0,2))
      memo
    end
  end

  if ruas.count <= vertices.count - 1
    return 0
  end

  tamanhos = ruas.map do |rua|
    rua[2]
  end.sort

  while tamanhos.count > vertices.count - 1
    total_economizado += tamanhos.pop
  end

  return total_economizado
  
end