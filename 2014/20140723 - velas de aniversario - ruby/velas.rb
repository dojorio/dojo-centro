def particao_de_velas(idades, velas)
  if idades.count == 1
    return 0 if velas.include?(idades[0])

    dif1 = (velas[0] * 10 + velas[1]) - idades[0]
    dif2 = (velas[1] * 10 + velas[0]) - idades[0]

    return [dif1.abs, dif2.abs].min
  end

  dif1 = velas.max - idades.max
  dif2 = velas.min - idades.min

  dif1.abs + dif2.abs
end