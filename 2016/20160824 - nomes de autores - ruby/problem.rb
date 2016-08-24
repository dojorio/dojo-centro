def nome_autor(nome)
  return nome.upcase unless nome.include?(' ')
  conjuncoes = 'da de'.split(' ')
  arr = 'junior filho'.upcase.split(' ') 
  nome = nome.split(" ")
  sobrenome = [nome.pop.upcase]

  if arr.include?(sobrenome.first)
  	sobrenome.unshift(nome.pop.upcase)
  end

  sobrenome.join(' ') + ", " +
  	nome.map do |p|
  		conjuncoes.include?(p) ?
  			p : p[0].upcase + p[1..-1]
  	end.join(' ')
end