def coelho(ovos, velocidade)
  tempo_restante = 720.0
  qnt_de_ovos = 0
  quantidade_de_ovos_a_pegar(ovos)
  velocidade_atual = velocidade / (2.0 ** (ovos.size))    

  posicao_atual = 0

  ovos.each do |ovo|
    distancia = ovo[1] - posicao_atual

    tempo_para_pegar_o_ovo = (distancia / velocidade_atual)

    if tempo_para_pegar_o_ovo <= tempo_restante
      velocidade_atual = velocidade_atual * 2
      qnt_de_ovos += 1
      tempo_restante -= tempo_para_pegar_o_ovo
      posicao_atual = ovo[1]
    end
  end

  qnt_de_ovos
end

def quantidade_de_ovos_a_pegar(ovos)
  qnt_ovos = 0
  return 1 if ovos.map { |ovo|  ovo[1] }.reduce(:+) < 720
end