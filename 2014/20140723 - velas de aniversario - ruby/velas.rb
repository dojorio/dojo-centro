def particao_de_velas(idades, velas)
  diffs = []

  # if idades.count == 1
    diffs << (velas[0] * 10 + velas[1]) - idades[0]
    diffs << (velas[1] * 10 + velas[0]) - idades[0]
    diffs << idades[0] - velas[0]
    diffs << idades[0] - velas[1]
  # end

  # if idades.count == 2
    diffs << (velas.max - idades.max).abs + (velas.min - idades.min).abs
  # end

  return diffs.map(&:abs).min
  
  # dif3 = (velas[0] * 10 + velas[1]) - idades[0]
  # dif4 = (velas[1] * 10 + velas[0]) - idades[0]
  
  # dif5 = (velas[0] * 10 + velas[1]) - idades[-1]
  # dif6 = (velas[1] * 10 + velas[0]) - idades[-1]

  #(dif1.abs + dif2.abs)

end