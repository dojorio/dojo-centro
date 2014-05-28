def salangram(salao, largura, comprimentos)

  #return salao.max if salao.min == 2
  if salao.min == 2
    salao.max
  else 
    'impossivel'
  end

  return 'impossivel' if comprimentos.size == 0

  comprimentos = comprimentos.sort.reverse
  salao_max = salao.max

  quantidade = 0

  comprimentos.each do |tabua|
    if salao_max >= tabua
      quantidade +=1
      salao_max -= tabua
    end
  end

  return quantidade if salao_max == 0

  comprimentos.shift
  salangram(salao, largura, comprimentos)
end
