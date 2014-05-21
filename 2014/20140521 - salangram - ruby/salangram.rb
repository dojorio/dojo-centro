def salangram(salao, largura, comprimentos)
  
  area_salao = salao[0] * salao[1]

  areas_tabuas = []
  largura /= 100
  for tabua in comprimentos
    areas_tabuas.push(largura * tabua)
  end

  for tabua in areas_tabuas 
    if(area_salao == tabua)
      1
    else
     'impossivel'
    end
  end

end
