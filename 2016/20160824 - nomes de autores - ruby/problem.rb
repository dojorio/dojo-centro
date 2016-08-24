def nome_autor(nome)
  return nome.upcase unless nome.include?(' ')
  nome = nome.split(" ")
  
  return nome.pop.upcase + ", " + nome.join(' ')
  
end