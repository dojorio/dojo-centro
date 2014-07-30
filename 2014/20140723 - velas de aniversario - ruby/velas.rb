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
    diffs << (velas.max - idades.max).abs +
     (velas.min - idades.min).abs
    
    idades = idades - velas
    diffs << idades.inject(:+)
  end

  return diffs.compact.map(&:abs).min
  
 
  $array = array(1, 2, 3);
  foreach ($array AS &$elemento) {
    $elemento *= 2;
  }
end