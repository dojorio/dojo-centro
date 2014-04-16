def coelho(ovos, velocidade)
  velocidade_atual = velocidade / 2

  if ovos.size == 2
    return 2
  end
  y = ovos[0][1]
  if y / velocidade_atual < 720
    1
  else
    0
  end
end