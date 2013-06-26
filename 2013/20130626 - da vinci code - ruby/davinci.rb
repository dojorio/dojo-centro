def davinci(chave, codigo)

  fib = [1, 2, 3]
  frase = ""

  fib.each do |n|
    chave.each_with_index do |x, i|
      if n==x
          frase << codigo[i]
      end
    end
  end
  return frase

  return chave.map {|x| codigo[x-1].chr }.join
end
