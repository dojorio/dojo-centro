def troca_ou_nao(rodadas)
  maior  = rodadas.size + 1
  trocas = 0
  
  while rodadas[0][0] != maior
    rodadas.shift
  end

  rodada = rodadas[0]

  if rodada[1] == 0 && rodada[0] == maior
    trocas += 1
  end

  if rodadas.size >1
    rodada = rodadas[1]
    if rodada[1] == 1 && rodada[0] != maior
      trocas += 1
    end
  end

  if rodadas.size >2
    if rodadas[2][1] == 1 && rodadas[2][0] != maior
      trocas += 1
    end
  end

  trocas
end