def particao_de_velas(idades, velas)
  if idades.count == 1
    return velas[0] * 10 + velas[1] - idades[0]
  end

  dif1 = velas.max - idades.max
  dif2 = velas.min - idades.min

  dif1.abs + dif2.abs
end