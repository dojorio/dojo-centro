def pintar(arvore)
  return 0 if arvore.empty?

  if arvore[1].empty?
    esquerda = 0
  else
    esquerda = arvore[1][0]
  end

  if arvore[2].empty?
    direita = 0
  else
    direita = arvore[2][0]
  end

  arvore[0] + 2 * [esquerda, direita].max + \
              3 * [esquerda, direita].min
end
