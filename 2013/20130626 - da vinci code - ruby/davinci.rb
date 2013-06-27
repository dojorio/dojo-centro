require 'generator'

def davinci(chave, codigo)
  codigo = codigo.chars.select{|x|('A'..'Z').include?(x)}.join

  lim_fib = (chave.max or 0)
  fib = Generator.new { |g|
    a = b = 1
    while a <= lim_fib
      a, b = a + b, a
      g.yield a
    end
  }

  mensagem = ''
  while fib.next?
    idx = chave.index(fib.next)
    if idx
      mensagem << codigo[idx].chr
    else
      mensagem << ' '
    end
  end
  mensagem
end

