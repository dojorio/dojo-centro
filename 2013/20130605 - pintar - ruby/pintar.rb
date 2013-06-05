def pintar(arvore)
  candidatos = [arvore]

  soma = 0
  tempo = 1
  while not candidatos.empty?
    maior = candidatos.max_by{|item| item[0]}

    soma += tempo * maior[0]
    tempo += 1

    candidatos.delete(maior)
    candidatos << maior[1]
    candidatos << maior[2]
  end

  soma
end
