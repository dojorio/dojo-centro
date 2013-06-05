def pintar(arvore)
  return 0 if arvore.nil?

  arvore[0] + 2 * [arvore[1][0],arvore[2][0]].max + 3 * [arvore[1][0],arvore[2][0]].min
end
