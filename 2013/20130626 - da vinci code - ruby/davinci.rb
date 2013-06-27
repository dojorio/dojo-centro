require 'generator'

def davinci(chave, codigo)
  codigo = codigo.chars.select{|x|('A'..'Z').include?(x)}.join

  lim_fib = (chave.max or 0)
  fib(lim_fib).map do |n|
    idx = chave.index(n)
    idx ? codigo[idx].chr : ' '
  end.join

end

def fib(limite)
  Generator.new { |g|
    a = b = 1
    while a <= limite
      g.yield a
      a, b = a + b, a
    end
  }
end
