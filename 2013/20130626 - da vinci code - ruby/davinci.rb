require 'generator'

def davinci(chave, codigo)
  codigo = codigo.gsub(/[^A-Z]/, '')

  fib(chave.max || 0).map do |n|
    idx = chave.index(n)
    idx ? codigo[idx].chr : ' '
  end.join

end

def fib(limite)
  Generator.new do |g|
    a = b = 1
    while a <= limite
      g.yield a
      a, b = a + b, a
    end
  end
end
