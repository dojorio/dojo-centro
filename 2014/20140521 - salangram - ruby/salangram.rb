def salangram(salao, largura, comprimentos)
  return 1 if comprimentos.index(salao.max)

  salao_max = salao.max
  soma = 0

  comprimentos.reverse.each do |tabua|
    if salao_max >= tabua
      soma +=1
      salao_max -= tabua
    end
  end

  return soma if salao_max == 0
  
  'impossivel'
end
