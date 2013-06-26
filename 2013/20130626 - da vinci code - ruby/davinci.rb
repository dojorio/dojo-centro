def davinci(chave, codigo)

  fib = [1, 2, 3, 5, 8]

  fib.map do |n|
    idx = chave.index(n)
    if idx
      codigo[idx].chr
    else
      ' '
    end
  end.join
end

def fib
  a = 1
  b = 2
  yield a
  yield b
  while true
    a = b
    b + a
    yield b

  end
end
