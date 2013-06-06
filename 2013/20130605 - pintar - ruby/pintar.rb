def maior_no(arvore)
  return 0 if arvore.empty?
  [arvore[0], maior_no(arvore[1]), maior_no(arvore[2])].max
end

def pintar(arvore)
  candidatos = [arvore]

  soma = 0
  tempo = 1

  while not candidatos.empty?
    maior = candidatos.max_by{ |item| maior_no(item) }

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
