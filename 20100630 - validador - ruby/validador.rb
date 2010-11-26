def validar(expressao)
  eh_numero = (expressao >= '0' and expressao <= '9')
  sinal = ['-','+']
  eh_numero or (sinal.include? expressao[0..0]  )
end

