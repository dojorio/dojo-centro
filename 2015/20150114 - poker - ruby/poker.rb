def maior_carta(mao)

  valor = lambda do |carta|
    '23456789TJQKA'.index(carta[0])
  end

  mao.reduce do |maior, carta|
    valor.(maior) > valor.(carta) ? maior : carta
  end
end

def valor(carta)
  '23456789TJQKA'.index(carta[0])
end