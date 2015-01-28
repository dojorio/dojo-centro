def maior_carta(mao)
  mao.reduce do |maior, carta|
    valor_da_carta(maior) > valor_da_carta(carta) ? maior : carta
  end
end

def valor_da_carta(carta)
  baralho = '23456789TJQKA'
  baralho.index(carta[0])
end


def compara_maos(mao1, mao2)
  maior_carta_mao1 = maior_carta(mao1)
  maior_carta_mao2 = maior_carta(mao2)
  
  if maior_carta([maior_carta_mao1, maior_carta_mao2]) == maior_carta_mao1
    return mao1
  else
    return mao2
  end

end