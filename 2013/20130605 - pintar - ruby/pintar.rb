def pintar(arvore)
  candidatos = [arvore]

  soma = 0
  tempo = 1
  while not candidatos.empty?
    maior = candidatos.max_by{|item| item[0] || 0}

    if not maior[0].nil?
      soma += tempo * maior[0]
      tempo += 1
      candidatos << maior[1]
      candidatos << maior[2]
    end

    candidatos.delete_at(candidatos.index(maior))
  end

  soma
end
