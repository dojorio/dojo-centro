def particao_de_velas(idades, velas)
  
  dif1 = velas.max - idades.max
  dif2 = velas.min - idades.min
  dif3 = velas.min - idades.max
  dif4 = velas.max - idades.min

  [(dif1.abs + dif2.abs), (dif3.abs + dif4.abs)].min
end