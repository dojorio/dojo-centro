def nome_autor(nome)
  return nome.upcase unless nome.include?(' ')
  nome = nome.split(" ")
  
  return nome.pop.upcase + ", " +
  	nome.map do |p|
  		if (p != 'da') 
  			p[0].upcase + p[1..-1]
  	    else
  	    	p
  		end
  	end.join(' ')
  
end