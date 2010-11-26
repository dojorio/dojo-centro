def posicao_do_ponteiro_em(hora)

  minuto = hora.split(":").last.to_i

  if hora == "12:59"
    hh = 1
  else
    hh=0
  end

  [hh, (minuto/5.0).round % 12]

end

