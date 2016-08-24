def nome_autor(nome)
  return nome.upcase unless nome.include?(' ')

  conjuncoes = 'da de'.split(' ')

  arr = 'junior filho'.split(' ') 
  nome = nome.downcase.split(' ')
  sobrenome = [nome.pop]

  if arr.include?(sobrenome.first)
  	sobrenome.unshift(nome.pop)
  end

  sobrenome.join(' ').upcase + ', ' +
  	nome.map do |p|
  		conjuncoes.include?(p) ?
  			p : p[0].upcase + p[1..-1]
  	end.join(' ')
end