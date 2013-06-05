def pintar(arvore)
  return 0 if arvore.empty?

  esquerda = arvore[1].empty? ? 0 : arvore[1][0]

  direita = arvore[2].empty? ? 0 : arvore[2][0]

  arvore[0] + 2 * [esquerda, direita].max + \
              3 * [esquerda, direita].min
end
