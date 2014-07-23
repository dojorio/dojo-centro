def particao_de_velas(idades, velas)
  
  dif1 = velas[0] - idades[0] 
  dif2 = velas[1] - idades[1] 

  (dif1.abs + dif2.abs)
end