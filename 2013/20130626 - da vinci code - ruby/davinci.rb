def davinci(chave, codigo)

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
