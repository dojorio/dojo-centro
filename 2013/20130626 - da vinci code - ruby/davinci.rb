def davinci(chave, codigo)
  codigo = codigo.chars.select{|x|('A'..'Z').include?(x)}.join

  lim_fib = (chave.max or 0)
  a = b = 1
  mensagem = ''
  while a <= lim_fib
    idx = chave.index(a)
    if idx
      mensagem << codigo[idx].chr
    else
      mensagem << ' '
    end
    a, b = a + b, a
  end
  mensagem
end
