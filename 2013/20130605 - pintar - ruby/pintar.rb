def pintar(arvore)
  return 0 if arvore.nil?

  arvore[0] + 2 * pintar(arvore[1]) + 2 * pintar(arvore[2])
end
