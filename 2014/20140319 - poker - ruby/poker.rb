
def tipo(mao)
  valores = mao.group_by { |carta| carta[0] }
               .values.map { |cartas| cartas.size }
               .select { |valor| valor > 1 }

  cartas_altas = {"T" => 10,"J" => 11,"Q" => 12,"K" => 13,"A" => 14}
  
  outros_valores = mao.map do |carta|
    cartas_altas.fetch(carta[0], carta[0].to_i)
  end.sort

  straight = outros_valores.last - outros_valores.first == 4
  flush    = mao.map{|carta| carta[1]}.uniq.count == 1
  royal    = outros_valores[0] == 10

  return 'royal flush' if royal && flush
  return 'straight flush' if straight && flush
  return 'straight' if straight
  return 'flush' if flush

  {
    [2] => 'par',
    [2, 2] => 'dois pares',
    [3] => 'trinca',
    [2, 3] => 'fullhouse',
    [4] => 'quadra',
  }.fetch(valores.sort, 'nada')

end
