def base10(a,b)
  a * 10 + b

end

def particao_de_velas(idades, velas)
  diffs = []

  if idades.count == 1
    diffs << base10(velas[0], velas[1]) - idades[0]
    diffs << base10(velas[1], velas[0]) - idades[0]
    diffs << idades[0] - velas[0]
    diffs << idades[0] - velas[1]
  end

  if idades.count == 2
    diffs << (velas.max - idades.max).abs + (velas.min - idades.min).abs
    diffs << base10(velas[0], velas[1]) - idades[0]
    diffs << base10(velas[1], velas[0]) - idades[0]
    diffs << base10(velas[0], velas[1]) - idades[1]
    diffs << base10(velas[1], velas[0]) - idades[1]
  end

  return diffs.map(&:abs).min
  
 
end