def troca_ou_nao(rodadas)
  maior  = rodadas.size + 1
  trocas = 0

  if rodadas[0][1] == 0 && rodadas[0][0] == maior
    trocas += 1
  end

  if rodadas.size == 2
    if rodadas[1][1] == 1 && rodadas[1][0] != maior 
      trocas += 1
    end

    if rodadas[1][1] == 0 && rodadas[1][0] == maior
      trocas += 1
    end
  end

  trocas
end