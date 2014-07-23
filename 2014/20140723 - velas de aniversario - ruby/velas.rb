def particao_de_velas(idades, velas)
  

  if idades.count == 1
    total = velas[0] * 10 + velas[1]
    return (total  - idades[0]).abs 
  end

  dif1 = velas.max - idades.max
  dif2 = velas.min - idades.min

  dif1.abs + dif2.abs
end