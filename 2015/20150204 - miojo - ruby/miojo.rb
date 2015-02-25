def tempo_preparo(miojo, ampulhetas)
  menor, maior = ampulhetas.min, ampulhetas.max

  ampulhetas_pares_e_miojo_impar = maior.even? && menor.even? && miojo.odd?

  if menor == maior || ampulhetas_pares_e_miojo_impar
    return "Pizza"
  end

  if maior % menor == miojo
    return maior
  end

  if (3*menor) - maior == miojo
    return 3*menor
  end

  menor * 2
end