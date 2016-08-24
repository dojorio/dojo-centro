def nome_autor(nome)
  nome = nome.split(" ")
  size = nome.size

  if size > 1
  	return nome[-1].upcase + ", " + nome[0] + (nome[1] != nome[-1] ? ' ' + nome[1] : '')
  end
  
  nome[-1].upcase
end