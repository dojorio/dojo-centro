def nome_autor(nome)
  return nome.upcase unless nome.include?(' ')
  conjuncoes = 'da de'.split(' ')
  nome = nome.split(" ")
  sobrenome = []
  if nome.last == "junior"

  nome.pop.upcase + ", " +
  	nome.map do |p|
  		conjuncoes.include?(p) ?
  			p : p[0].upcase + p[1..-1]
  	end.join(' ')
end