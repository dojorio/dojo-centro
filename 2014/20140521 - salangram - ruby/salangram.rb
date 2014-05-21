def salangram(salao, largura, comprimentos)
  area_tabua = largura / 100 * comprimentos[0]
  area_salao = salao[0] * salao[1]

  if(area_salao == area_tabua)
    1
  else
   'impossivel'
  end
end
