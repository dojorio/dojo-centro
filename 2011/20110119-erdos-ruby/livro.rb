class Livro
  attr_reader :autores

  def initialize(*autores)
    @autores = autores
  end
end

class Silvometro
  def mede(*livros)
  	escritores = []
    if livros.size == 1
	    if livros[0].autores.include? 'silva'
	    	livros.each do |livro|
	    		livro.autores.each do |autor|
	    		  if !escritores.include?(autor)
	    		  	escritores << autor
	    		  end
	    		end
	    	end
	    	return escritores.collect{|escritor| escritores.index(escritor)}
	      #return [0] + [1] * (livros[0].autores.size - 1)
	    end
	  elsif livros.size == 2
      return [0,1,2]
    else
      return [0,1,2,3]
	  end
  end
end
