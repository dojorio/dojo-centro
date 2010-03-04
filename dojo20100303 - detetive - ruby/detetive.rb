class Object
  def exist?
    not self.nil?
  end
end

class CenaCrime
	def initialize(assassino, vitima, detetive = nil)
  	  assassino.tenta_matar vitima
	  detetive.prende(assassino) if detetive.exist?
	end
end

class Assassino
  attr_writer :preso
  def initialize
	@preso = false
  end
  def tenta_matar(pessoa)
    pessoa.morreu = pessoa.kind_of? Vitima
    if pessoa.kind_of? Detetive
		pessoa.prende self
	end
  end
  def preso?
    @preso
  end
end

class Pessoa
  attr_writer :morreu
  def initialize
	@morreu = false
  end
  
  def morreu?
    @morreu
  end
end

class Vitima < Pessoa; end;

class Detetive < Pessoa
  def prende(assassino)
	assassino.preso = true
  end
end