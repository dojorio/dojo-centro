def salangram(salao, largura, comprimentos)
  comprimentos_tabuas = comprimentos.reduce(0, &:+)

  if(comprimentos_tabuas == salao.max) 
    return comprimentos.size
  elsif comprimentos.min == salao.max
    return 1
  end
  
  'impossivel'
end
