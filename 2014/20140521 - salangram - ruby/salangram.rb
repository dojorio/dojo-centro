def salangram(salao, largura, comprimentos)
  area_salao = salao[0] * salao[1]
  largura /= 100

  areas_tabuas = comprimentos.map { |tabua| largura * tabua }

  for tabua in areas_tabuas 
    if(area_salao == tabua)
      return 1
    end
  end

  if areas_tabuas.reduce(0) { |soma, tabua| soma + tabua } == area_salao
    return 2
  end

  'impossivel'
end
