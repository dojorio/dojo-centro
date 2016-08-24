def nome_autor(nome)
  return nome.upcase unless nome.contains?(' ')
  nome = nome.split(" ")

  if nome.size > 1
  	return nome.pop.upcase + ", " + nome.join(' ')
  end

  nome.last.upcase
end