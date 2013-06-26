def davinci(chave, codigo)

  limFib = chave.max
  fib(limFib).map do |n|
    idx = chave.index(n)
    if idx
      codigo[idx].chr
    else
      ' '
    end
  end.join
end

#saida[fib.chave[i].search] = codigo[i]

def fib(limite)
  fib = [1,2]

  limite.times do
    fib[2] = fib[0]+fib[1]
  end
end
