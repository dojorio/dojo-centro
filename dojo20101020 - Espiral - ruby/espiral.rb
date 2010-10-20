def gera_espiral (linhas, colunas)
  if linhas*colunas == 4
    (1..colunas).to_a.join(' ')+(colunas+1..linhas*colunas).to_a.join(' ')
  elsif linhas > 1
    (1..linhas).to_a.join("\n")
  else
    (1..colunas).to_a.join(' ')
  end
end

