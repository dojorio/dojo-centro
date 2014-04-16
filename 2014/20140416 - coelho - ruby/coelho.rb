def coelho(ovos, velocidade)
  velocidade_atual = velocidade / 2
  tempo_restante = 720
  qnt_de_ovos = 0

  ovos.each do |ovo|
    distancia = ovo[1]
    tempo_para_pegar_o_ovo = (distancia / velocidade_atual)

    if tempo_para_pegar_o_ovo < tempo_restante
      qnt_de_ovos += 1
      tempo_restante -= tempo_para_pegar_o_ovo
    end
  end

  qnt_de_ovos
end