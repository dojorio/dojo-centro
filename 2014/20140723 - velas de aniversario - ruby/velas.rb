def particao_de_velas(idades, velas)
  if idades.count == 1
    return 0 if velas.include?(idades[0])

    dif1 = (velas[0] * 10 + velas[1]) - idades[0]
    dif2 = (velas[1] * 10 + velas[0]) - idades[0]

    if((velas[0] + velas[1]) == idades[0])
      return velas.min
    end

    dif3 = idades[0] - velas[0]
    dif4 = idades[0] - velas[1]

    return [dif1.abs, dif2.abs].min
  end

  dif1 = velas.max - idades.max
  dif2 = velas.min - idades.min
  
  # dif3 = (velas[0] * 10 + velas[1]) - idades[0]
  # dif4 = (velas[1] * 10 + velas[0]) - idades[0]
  
  # dif5 = (velas[0] * 10 + velas[1]) - idades[-1]
  # dif6 = (velas[1] * 10 + velas[0]) - idades[-1]

  (dif1.abs + dif2.abs)

end