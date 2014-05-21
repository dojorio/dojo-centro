def salangram(salao, largura, comprimentos)
  return 1 if comprimentos.index(salao.max)

  comprimentos_tabuas = comprimentos.reduce(0, &:+)

  if(comprimentos_tabuas == salao.max) 
    return comprimentos.size
  end
  
  'impossivel'
end
