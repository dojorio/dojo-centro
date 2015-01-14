def maior_carta(mao)
  mao.reduce do |maior, carta|
    valor_da_carta(maior) > valor_da_carta(carta) ? maior : carta
  end
end

def valor_da_carta(carta)
  baralho = '23456789TJQKA'
  baralho.index(carta[0])
end