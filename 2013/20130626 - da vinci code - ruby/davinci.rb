def davinci(chave, codigo)

  fib = 1..(chave.max or 0)

  fib.map do |n|
    idx = chave.index(n)
    if idx
      codigo[idx].chr
    else
      ' '
    end
  end.join
end
